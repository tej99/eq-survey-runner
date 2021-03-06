import unittest

from app import create_app
from app.forms.household_relationship_form import build_relationship_choices, deserialise_relationship_answers, serialise_relationship_answers, generate_relationship_form
from app.data_model.answer_store import AnswerStore, Answer
from app.schema_loader.schema_loader import load_schema_file
from app.helpers.schema_helper import SchemaHelper
from app.questionnaire.location import Location


class TestHouseholdRelationshipForm(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SERVER_NAME'] = "test"
        self.app_context = self.app.app_context()
        self.app_context.push()

    @staticmethod
    def _error_exists(answer_id, msg, mapped_errors):
        return any(a_id == answer_id and msg in ordered_errors for a_id, ordered_errors in mapped_errors)

    def test_build_relationship_choices(self):
        answer_store = AnswerStore([
            {
                'answer_id': 'first-name',
                'block_id': 'household-composition',
                'value': 'Joe',
                'answer_instance': 0,
            }, {
                'answer_id': 'last-name',
                'block_id': 'household-composition',
                'value': 'Bloggs',
                'answer_instance': 0,
            }, {
                'answer_id': 'first-name',
                'block_id': 'household-composition',
                'value': 'Jane',
                'answer_instance': 1,
            }, {
                'answer_id': 'last-name',
                'block_id': 'household-composition',
                'value': 'Bloggs',
                'answer_instance': 1,
            }, {
                'answer_id': 'first-name',
                'block_id': 'household-composition',
                'value': 'Bob',
                'answer_instance': 2,
            }, {
                'answer_id': 'last-name',
                'block_id': 'household-composition',
                'value': '',
                'answer_instance': 2,
            }
        ])

        choices = build_relationship_choices(answer_store, 0)

        expected_choices = [
            ('Joe Bloggs', 'Jane Bloggs'),
            ('Joe Bloggs', 'Bob'),
        ]

        self.assertEqual(expected_choices, choices)

        # Check each group is correct
        choices = build_relationship_choices(answer_store, 1)

        expected_choices = [
            ('Jane Bloggs', 'Bob'),
        ]

        self.assertEqual(expected_choices, choices)

    def test_generate_relationship_form_creates_empty_form(self):
        survey = load_schema_file("test_relationship_household.json")
        block_json = SchemaHelper.get_block(survey, 'relationships')
        error_messages = SchemaHelper.get_messages(survey)

        answer = SchemaHelper.get_first_answer_for_block(block_json)

        form = generate_relationship_form(block_json, 3, {}, error_messages=error_messages)

        self.assertTrue(hasattr(form, answer['id']))
        self.assertEqual(len(form.data[answer['id']]), 3)

    def test_generate_relationship_form_creates_form_from_data(self):
        survey = load_schema_file("test_relationship_household.json")
        block_json = SchemaHelper.get_block(survey, 'relationships')
        error_messages = SchemaHelper.get_messages(survey)

        answer = SchemaHelper.get_first_answer_for_block(block_json)

        form = generate_relationship_form(block_json, 3, {
            '{answer_id}-0'.format(answer_id=answer['id']): 'Husband or Wife',
            '{answer_id}-1'.format(answer_id=answer['id']): 'Brother or Sister',
            '{answer_id}-2'.format(answer_id=answer['id']): 'Relation - other',
        }, error_messages=error_messages)

        self.assertTrue(hasattr(form, answer['id']))

        expected_form_data = ['Husband or Wife', 'Brother or Sister', 'Relation - other']
        self.assertEqual(form.data[answer['id']], expected_form_data)

    def test_generate_relationship_form_errors_are_correctly_mapped(self):
        survey = load_schema_file("test_relationship_household.json")
        block_json = SchemaHelper.get_block(survey, 'relationships')
        error_messages = SchemaHelper.get_messages(survey)

        answer = SchemaHelper.get_first_answer_for_block(block_json)

        form = generate_relationship_form(block_json, 3, {
            '{answer_id}-0'.format(answer_id=answer['id']): '1',
            '{answer_id}-1'.format(answer_id=answer['id']): '3',
        }, error_messages=error_messages)

        form.validate()
        mapped_errors = form.map_errors()

        message = "Not a valid choice"

        self.assertTrue(self._error_exists(answer['id'], message, mapped_errors))

    def test_serialise_relationship_answers(self):
        location = Location("household-relationships", 0, "relationships")

        field_data = ['Husband or Wife', 'Son or daughter', 'Unrelated']

        actual_answers = serialise_relationship_answers(location, 'who-is-related', field_data)

        expected_answers = [
            {
                'group_id':"household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 0,
                'value': 'Husband or Wife'
            }, {
                'group_id':"household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 1,
                'value': 'Son or daughter'
            }, {
                'group_id': "household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 2,
                'value':'Unrelated'
            }
        ]

        for answer in actual_answers:
            self.assertIn(answer.__dict__, expected_answers)

    def test_deserialise_relationship_answers(self):

        expected_form_data = {
            'who-is-related-0': 'Husband or Wife',
            'who-is-related-1': 'Son or daughter',
            'who-is-related-2': 'Unrelated',
        }

        serialised_answers = [
            {
                'group_id':"household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 0,
                'value': 'Husband or Wife'
            }, {
                'group_id':"household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 1,
                'value': 'Son or daughter'
            }, {
                'group_id': "household-relationships",
                'group_instance': 0,
                'block_id': 'relationships',
                'answer_id': 'who-is-related',
                'answer_instance': 2,
                'value':'Unrelated'
            }
        ]

        deserialised_form_data = deserialise_relationship_answers(serialised_answers)

        self.assertEquals(expected_form_data, deserialised_form_data)
