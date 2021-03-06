from flask_wtf import FlaskForm
from wtforms import FieldList, Form, FormField, StringField
from wtforms import validators

from app.data_model.answer_store import Answer
from app.helpers.schema_helper import SchemaHelper

from werkzeug.datastructures import MultiDict


def get_name_form(block_json, error_messages):
    class NameForm(Form):
        pass

    for answer in SchemaHelper.get_answers_for_block(block_json):
        validate_with = [validators.optional()]

        if answer['mandatory'] is True:
            error_message = error_messages['MANDATORY']
            if 'validation' in answer and 'messages' in answer['validation'] \
                    and 'MANDATORY' in answer['validation']['messages']:
                error_message = answer['validation']['messages']['MANDATORY']

            validate_with = [validators.InputRequired(
                message=error_message,
            )]

        # Have to be set this way given hyphenated names
        # are considered invalid in python
        field = StringField(validators=validate_with)

        setattr(NameForm, answer['id'], field)

    return NameForm


def serialise_composition_answers(location, data):
    answers = []
    for index, person_data in enumerate(data):
        for answer_id in person_data.keys():
            answer = Answer(
                location=location,
                answer_id=answer_id,
                answer_instance=index,
                value=person_data[answer_id],
            )
            answers.append(answer)
    return answers


def deserialise_composition_answers(answers):
    household = {}

    for answer in answers:
        composition_id = 'household-{index}-{subfield}'.format(
            index=answer['answer_instance'],
            subfield=answer['answer_id'],
        )
        household[composition_id] = answer['value']

    return household


def map_field_errors(errors, index):
    ordered_errors = []
    for subfield, errorlist in errors.items():
        answer_id = 'household-{index}-{subfield}'.format(index=index, subfield=subfield)
        for error in errorlist:
            ordered_errors.append((answer_id, error))
    return ordered_errors


def generate_household_composition_form(block_json, data, error_messages):
    class HouseHoldCompositionForm(FlaskForm):
        household = FieldList(FormField(get_name_form(block_json, error_messages)), min_entries=1)

        def map_errors(self):
            ordered_errors = []

            if 'household' in self.errors and len(self.errors['household']) > 0:
                for index, field in enumerate(self.household):
                    ordered_errors += map_field_errors(field.errors, index)
            return ordered_errors

        def answer_errors(self, input_id):
            return [error[1] for error in self.map_errors() if input_id == error[0]]

        def remove_person(self, index_to_remove):
            popped = []

            assert len(self.household.data) >= index_to_remove, "Expected household data length >= index to remove"

            while index_to_remove != len(self.household.data):
                popped.append(self.household.pop_entry())

            popped.reverse()

            for field in popped[1:]:
                self.household.append_entry(field.data)

        def serialise(self, location):
            """
            Returns a list of answers representing the form data
            :param location: The location to associate the form data with
            :return:
            """
            return serialise_composition_answers(location, self.household.data)

    return HouseHoldCompositionForm(MultiDict(data), meta={'csrf': False})
