import unittest
from translations.extract_translation_data import *
from mock import mock_open, patch

data = {
    "options": [
        {
            "label": "Yes",
            "value": "No"
        }
    ],
    "validation": {
        "messages": {
            "mandatory": "message here"
        }
    },
    "guidance": [
        {
            "label": "guidance text"
        }
    ],
    "title": "this is a title",
    "description": "this is a description"
}


class ExtractTranslationTest(unittest.TestCase):
    def test_get_text_for_container(self):
        get_container_text = get_text_for_container({"label": "hello"})
        self.assertEqual(get_container_text, ['hello'])

# test these three with no data to show it can be handled
    def test_get_options_text_in_answer(self):
        get_option_text = get_options_text_in_answer('')
        self.assertEqual(get_option_text, [])

    def test_get_validation_text_in_answer(self):
        get_validation_text = get_validation_text_in_answer('')
        self.assertEqual(get_validation_text, [])

    def test_get_guidance_text_in_question(self):
        get_guidance_text = get_guidance_text_in_question('')
        self.assertEqual(get_guidance_text, [])

# test the same three with relevant data
    def test_get_options_text_in_answer2(self):
        get_option_text2 = get_options_text_in_answer(data)
        self.assertEqual(get_option_text2, ['Yes'])

    def test_get_validation_text_in_answer2(self):
        get_validation_text2 = get_validation_text_in_answer(data)
        self.assertEqual(get_validation_text2, ['message here'])

    def test_get_guidance_text_in_question2(self):
        get_guidance_text2 = get_guidance_text_in_question(data)
        self.assertEqual(get_guidance_text2, ['guidance text'])


# test to get all header data (no key available)
    def test_get_header_text(self):
        get_all_header_text = get_header_text(data)
        self.assertEqual(get_all_header_text, ['this is a title'])


if __name__ == '__main__':
    unittest.main()
