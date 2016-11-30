import unittest
from collections import OrderedDict

import re
import os
import click
from click.testing import CliRunner
import json
from mock import mock_open, patch
from translate_schema_v2 import deserialise_json


class TestLoadTranslation(unittest.TestCase):

    def test_deserialise_json(self):
        mock = mock_open(read_data='{"title": "Survey"}')
        with patch('builtins.open', mock, create=True):
            deserialised_json_data = deserialise_json('sample.json')
            self.assertEqual(deserialised_json_data['title'], 'Survey')

    def test_deserialise_json_raises_exception(self):
        mock = mock_open(read_data='{"title": "Survey"')
        with patch('builtins.open', mock, create=True):
            self.assertRaises(ValueError, deserialise_json('sample.json'))


if __name__ == '__main__':
    unittest.main()
