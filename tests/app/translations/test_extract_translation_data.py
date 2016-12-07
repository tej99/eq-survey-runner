import unittest
from translations.extract_translation_data import *
import os
import json


class ExtractTranslationTest(unittest.TestCase):
    def test_get_text_for_container(self):
        get_container_text = get_text_for_container({"label": "hello"})
        self.assertEqual(get_container_text, ['hello'])

    def test_get_text(self):
        get_all_text = get_text('')
        self.assertEqual(get_all_text, '')

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
        get_option_text2 = get_options_text_in_answer('')
        self.assertEqual(get_option_text2, [])

    def test_get_validation_text_in_answer2(self):
        get_validation_text2 = get_validation_text_in_answer('')
        self.assertEqual(get_validation_text2, [])

    def test_get_guidance_text_in_question2(self):
        get_guidance_text2 = get_guidance_text_in_question('')
        self.assertEqual(get_guidance_text2, [])

# test to get all header data (no key available)
    def test_get_header_text(self):
        get_all_header_text = get_header_text('mock?')
        self.assertEqual(get_all_header_text, ['mock?'])

if __name__ == '__main__':
    unittest.main()
