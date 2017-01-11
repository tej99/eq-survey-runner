import calendar
import logging

from app.helpers.schema_helper import SchemaHelper
from app.jinja_filters import format_household_member_name
from app.validation.error_messages import error_messages
from app.validation.validators import positive_integer_type_check, date_check, month_year_check, DateRangeCheck

from flask_wtf import FlaskForm

from wtforms import FieldList, Form, FormField, IntegerField, SelectField, SelectMultipleField, StringField, TextAreaField
from wtforms import validators
from wtforms.widgets import CheckboxInput, ListWidget, RadioInput, TextArea, TextInput


logger = logging.getLogger(__name__)


def build_relationship_choices(answer_store, group_instance):
    household_answers = answer_store.filter(answer_id='household')

    first_names = [answer['first_name'] for answer in household_answers[0]['value']]
    last_names = [answer['last_name'] for answer in household_answers[0]['value']]

    household_members = []

    for first_name, last_name in zip(first_names, last_names):
        household_members.append({
            'first-name': first_name,
            'last-name': last_name,
        })

    remaining_people = household_members[group_instance + 1:] if group_instance < len(household_members) else []

    current_person_name = format_household_member_name([
        household_members[group_instance]['first-name'],
        household_members[group_instance]['last-name'],
    ])

    choices = []

    for index, remaining_person in enumerate(remaining_people):
        other_person_name = format_household_member_name([
            remaining_person['first-name'],
            remaining_person['last-name'],
        ])
        choices.append((current_person_name, other_person_name))

    return choices


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def get_date_form(to_field_data=None, validate_range=False):
    class DateForm(Form):

        MONTH_CHOICES = [('', 'Select month')] + [(str(x), calendar.month_name[x]) for x in range(1, 13)]

        month = SelectField(choices=MONTH_CHOICES, default='')
        year = StringField()

    if validate_range and to_field_data:
        DateForm.day = StringField(validators=[date_check, DateRangeCheck(to_field_data=to_field_data)])
    else:
        DateForm.day = StringField(validators=[date_check])

    return DateForm


class MonthYearDateForm(Form):

    MONTH_CHOICES = [('', 'Select month')] + [(str(x), calendar.month_name[x]) for x in range(1, 13)]

    month = SelectField(choices=MONTH_CHOICES, default='', validators=[month_year_check])
    year = StringField()


class NameForm(Form):
    first_name = StringField(validators=[
        validators.InputRequired(
            message=error_messages['MANDATORY'],
        ),
    ])

    middle_names = StringField(validators=[validators.Optional()])
    last_name = StringField(validators=[validators.Optional()])


def get_date_range_fields(question_json, to_field_data):
    answer_from = question_json['answers'][0]
    answer_to = question_json['answers'][1]

    field_from = FormField(
        get_date_form(to_field_data=to_field_data, validate_range=True),
        label=answer_from['label'] if 'label' in answer_from else '',
        description=answer_from['guidance'] if 'guidance' in answer_from else '',
    )
    field_to = FormField(
        get_date_form(),
        label=answer_to['label'] if 'label' in answer_to else '',
        description=answer_to['guidance'] if 'guidance' in answer_to else '',
    )

    return field_from, field_to


class HouseHoldCompositionForm(FlaskForm):
    household = FieldList(FormField(NameForm), min_entries=1)

    def remove_person(self, index_to_remove):
        popped = []

        while index_to_remove != len(self.household.data):
            popped.append(self.household.pop_entry())

        popped.reverse()

        for field in popped[1:]:
            self.household.append_entry(field.data)


def generate_relationship_form(block_json, number_of_entries, data):
    class HouseHoldRelationshipForm(FlaskForm):
        pass

    answer = SchemaHelper.get_first_answer_for_block(block_json)
    guidance = answer['guidance'] if 'guidance' in answer else ''
    label = answer['label'] if 'label' in answer else ''

    field = FieldList(SelectField(
        label=label,
        description=guidance,
        choices=build_choices(answer['options']),
        widget=ListWidget(),
        option_widget=RadioInput(),
    ), min_entries=number_of_entries)

    setattr(HouseHoldRelationshipForm, answer['id'], field)

    if data:
        data_class = Struct(**data)
        form = HouseHoldRelationshipForm(csrf_enabled=False, obj=data_class)
    else:
        form = HouseHoldRelationshipForm(csrf_enabled=False)

    return form


def get_date_data(form_data, answer_id):
    day_id = answer_id + '-day'
    month_id = answer_id + '-month'
    year_id = answer_id + '-year'

    if all(x in form_data for x in [day_id, month_id, year_id]):
        return {
            'day': form_data[day_id],
            'month': form_data[month_id],
            'year': form_data[year_id],
        }
    return None


def generate_form(block_json, data):
    class QuestionnaireForm(FlaskForm):
        pass

    for section in block_json['sections']:
        for question in section['questions']:
            if question['type'] == 'DateRange':
                to_field_id = question['answers'][1]['id']
                to_field_data = get_date_data(data, to_field_id)

                from_field, to_field = get_date_range_fields(question, to_field_data)

                setattr(QuestionnaireForm, question['answers'][0]['id'], from_field)
                setattr(QuestionnaireForm, question['answers'][1]['id'], to_field)
            else:
                for answer in question['answers']:
                    name = answer['label'] if 'label' in answer else question['title']
                    setattr(QuestionnaireForm, answer['id'], get_field(answer, name))
    if data:
        data_class = Struct(**data)
        form = QuestionnaireForm(csrf_enabled=False, obj=data_class)
    else:
        form = QuestionnaireForm(csrf_enabled=False)

    return form


def get_field(answer, label):
    field = None
    guidance = answer['guidance'] if 'guidance' in answer else ''

    if answer['type'] == 'Radio':
        field = SelectField(
            label=label,
            description=guidance,
            choices=build_choices(answer['options']),
            widget=ListWidget(),
            option_widget=RadioInput(),
        )
    if answer['type'] == 'Checkbox':
        field = SelectMultipleField(
            label=label,
            description=guidance,
            choices=build_choices(answer['options']),
            widget=ListWidget(),
            option_widget=CheckboxInput(),
        )
    if answer['type'] == 'Date':
        field = FormField(
            get_date_form(),
            label=label,
            description=guidance,
        )
    if answer['type'] == 'MonthYearDate':
        field = FormField(
            MonthYearDateForm,
            label=label,
            description=guidance,
        )
    if answer['type'] == 'Currency':
        if answer['mandatory'] is True:
            field = IntegerField(
                label=label,
                description=guidance,
                widget=TextInput(),
                validators=[
                    validators.InputRequired(
                        message=answer['validation']['messages']['MANDATORY'] or error_messages['MANDATORY']
                    ),
                    positive_integer_type_check,
                ],
            )
        else:
            field = IntegerField(
                label=label,
                description=guidance,
                widget=TextInput(),
                validators=[
                    validators.Optional(),
                ],
            )
    if answer['type'] == 'PositiveInteger' or answer['type'] == 'Integer':
        if answer['mandatory'] is True:
            field = IntegerField(
                label=label,
                description=guidance,
                widget=TextInput(),
                validators=[
                    validators.InputRequired(
                        message=answer['validation']['messages']['MANDATORY'] or error_messages['MANDATORY']
                    ),
                ],
            )
        else:
            field = IntegerField(
                label=label,
                description=guidance,
                widget=TextInput(),
                validators=[
                    validators.Optional(),
                ],
            )
    if answer['type'] == 'TextArea':
        field = TextAreaField(
            label=label,
            description=guidance,
            widget=TextArea(),
            validators=[
                validators.Optional(),
            ],
            filters=[lambda x: x if x else None],
        )
    if answer['type'] == 'TextField':
        field = StringField(
            label=label,
            description=guidance,
            widget=TextArea(),
            validators=[
                validators.Optional(),
            ],
        )

    if field is None:
        logger.info("Could not find field for answer type %s", answer['type'])

    return field


def build_choices(options):
    choices = []
    for option in options:
        choices.append((option['label'], option['value']))
    return choices
