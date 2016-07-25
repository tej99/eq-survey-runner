from app.schema.answers.integer_answer import IntegerAnswer
import unittest


class TestIntegerAnswer(unittest.TestCase):
    def test_get_typed_value(self):
        answer = IntegerAnswer()
        answer.id = 'some_int'

        # Data should come in as a string, mimicking http request data
        post_vars = {
            'some_int': '3'
        }

        typed_value = answer.get_typed_value(post_vars)

        self.assertIsInstance(typed_value, int)
        self.assertEquals(typed_value, 3)

    def test_missing_value(self):
        answer = IntegerAnswer()
        answer.id = 'some_int'

        post_vars = {}

        typed_value = answer.get_typed_value(post_vars)

        self.assertIsNone(typed_value)

    def test_invalid_value(self):
        answer = IntegerAnswer()
        answer.id = 'some_int'

        post_vars = {
            'some_int': 'not an int'
        }

        self.assertRaises(Exception, answer.get_typed_value, post_vars)
