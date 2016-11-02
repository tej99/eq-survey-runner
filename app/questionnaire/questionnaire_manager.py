import logging

from app.globals import get_answers, get_questionnaire_store
from app.piping.plumbing_preprocessor import PlumbingPreprocessor
from app.questionnaire.navigator import Navigator, evaluate_rule
from app.questionnaire.user_action_processor import UserActionProcessor, UserActionProcessorException

from app.templating.template_register import TemplateRegistry

from flask_login import current_user

logger = logging.getLogger(__name__)


class InvalidLocationException(Exception):
    pass


class QuestionnaireManager(object):
    '''
    This class represents a user journey through a survey. It models the request/response process of the web application
    '''
    def __init__(self, schema, submitted_at=None, json=None):
        self.submitted_at = submitted_at
        self._json = json
        self._schema = schema
        self.state = None

        self.navigator = Navigator(self._json)

    def validate(self, location, post_data):

        if location in self.navigator.get_location_path(get_answers(current_user)):

            self.build_state(location, post_data)

            if self.state:
                self._conditional_display(self.state)
                is_valid = self.state.schema_item.validate(self.state)
                # Todo, this doesn't feel right, validation is casting the user values to their type.

                return is_valid

            else:
                # Item has node, but is not in schema: must be introduction, thank you or summary
                return True
        else:
            # Not a validation location, so can't be valid
            return False

    def validate_all_answers(self):

        for location in self.navigator.get_location_path(get_answers(current_user)):
            is_valid = self.validate(location, get_answers(current_user))

            if not is_valid:
                logger.debug("Failed validation with current location %s", location)
                return False, location

        return True, None

    def process_incoming_answers(self, location, post_data):
        logger.debug("Processing post data for %s", location)

        # process incoming post data
        user_action = self._get_user_action(post_data)

        is_valid = self.validate(location, post_data)
        # run the validator to update the validation_store
        if is_valid:

            # Store answers in QuestionnaireStore
            questionnaire_store = get_questionnaire_store(current_user.user_id, current_user.user_ik)

            if location not in questionnaire_store.visited_blocks:
                questionnaire_store.visited_blocks.append(location)

            questionnaire_store.save()

            # process the user action
            try:
                user_action_processor = UserActionProcessor(self._schema, self)
                user_action_processor.process_action(user_action)

            except UserActionProcessorException as e:
                logger.error("Error processing user actions")
                logger.exception(e)
                return False, e.next_location

        return is_valid, None

    def get_rendering_context(self, location, is_valid=True):

        if is_valid:
            if location == 'summary':
                return self._get_summary_rendering_context()
            else:
                # apply page answers?
                self.build_state(location, get_answers(current_user))

        if self.state:
            self._plumbing_preprocessing(self.state)
            self._conditional_display(self.state)

        previous_location = self.navigator.get_previous_location(get_answers(current_user), location)

        # look up the preprocessor and then build the view data
        preprocessor = TemplateRegistry.get_template_preprocessor(location)
        return preprocessor.build_view_data(self._schema, [self.state], previous_location)

    def _get_summary_rendering_context(self):
        state_items = []

        for location in self.navigator.get_location_path(get_answers(current_user)):
            self.build_state(location, get_answers(current_user))
            if self.state:
                self._plumbing_preprocessing(self.state)
                self._conditional_display(self.state)
                state_items.append(self.state)

        previous_location = self.navigator.get_previous_location(get_answers(current_user), "summary")

        # look up the preprocessor and then build the view data
        preprocessor = TemplateRegistry.get_template_preprocessor('summary')
        return preprocessor.build_view_data(self._schema, state_items, previous_location)

    def build_state(self, item_id, answers):
        # Build the state from the linked list and the answers
        self.state = None
        if self._schema.item_exists(item_id):
            schema_item = self._schema.get_item_by_id(item_id)
            self.state = schema_item.construct_state()
            self.state.update_state(answers)

    def _plumbing_preprocessing(self, state):
        # Run the current state through the plumbing preprocessor
        plumbing_template_preprocessor = PlumbingPreprocessor()
        plumbing_template_preprocessor.plumb_current_state(self, self.state, self._schema)

    def _conditional_display(self, item):
        # Process any conditional display rules

        if item.schema_item:

            item.skipped = False

            if hasattr(item.schema_item, 'skip_condition') and item.schema_item.skip_condition:
                rule = item.schema_item.skip_condition.__dict__
                # Sometimes its a dict and sometimes its an object?
                rule['when'] = rule['when'].__dict__ if not isinstance(rule['when'], dict) else rule['when']
                answer = get_answers(current_user).get(rule['when']['id'])

                item.skipped = evaluate_rule(rule, answer)

            for child in item.children:
                self._conditional_display(child)

    def _get_user_action(self, post_data):
        user_action = None

        for key in post_data.keys():
            if key.startswith('action['):
                # capture the required action
                user_action = key[7:-1]

        return user_action

    def get_schema_item_by_id(self, item_id):
        return self._schema.get_item_by_id(item_id)
