from app.schema.answer import Answer
from app.questionnaire_state.answer import Answer as State
import unittest


class AnswerModelTest(unittest.TestCase):
    def test_basics(self):
        answer = Answer()

        answer.id = 'some-id'
        answer.label = 'my answer object'
        answer.guidance = 'fill this in'
        answer.type = 'some-type'
        answer.code = 'code'
        answer.container = None

        self.assertEquals(answer.id, 'some-id')
        self.assertEquals(answer.label, 'my answer object')
        self.assertEquals(answer.guidance, 'fill this in')
        self.assertEquals(answer.type, 'some-type')
        self.assertEquals(answer.code, 'code')
        self.assertIsNone(answer.container)

    def test_construct_state(self):
        answer = Answer()

        answer.id = 'some-id'
        state = answer.construct_state()

        self.assertIsInstance(state, State)
        self.assertEquals(state.id, answer.id)
        self.assertIsNone(state.errors)
        self.assertIsNone(state.warnings)
        self.assertIsNone(state.value)

    def test_get_state_class(self):
        answer = Answer()

        state_class = answer.get_state_class()

        self.assertEquals(state_class, State)
