import unittest
from translations.extract_translation_data import *
import re
import json


def regular_expression(line):
    re_tester = re.split('({{.+?}})', line, maxsplit=1)
    return re_tester


class ManipulateTranslationTest(unittest.TestCase):
    def test_remove_duplicates(self):
        test_duplication = remove_duplicates('aaaaaaaaa')
        self.assertEqual(test_duplication, {'a'})

    def test_sort(self):
        test_sorting = sort_text('helloo')
        # takes out the string, removes duplicates and sorts in reverse
        self.assertEqual(test_sorting, ['h', 'e', 'l', 'l', 'o', 'o'])

    def test_regex(self):
        # checks a string for anything between {{}} and splits
        reg_ex = regular_expression('start {{exercise.start_date|pretty_date}} end')
        self.assertEquals(reg_ex, ['start ', '{{exercise.start_date|pretty_date}}', ' end'])


if __name__ == '__main__':
    unittest.main()
