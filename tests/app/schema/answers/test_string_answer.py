from app.schema.answers.string_answer import StringAnswer
import unittest


class StringAnswerTest(unittest.TestCase):
    def test_get_typed_value(self):
        answer = StringAnswer()
        answer.id = 'string'

        post_vars = {
            'string': 'string value'
        }

        self.assertEquals(answer.get_typed_value(post_vars), 'string value')

    def test_get_missing_value(self):
        answer = StringAnswer()
        answer.id = 'string'

        post_vars = {}

        self.assertIsNone(answer.get_typed_value(post_vars))
