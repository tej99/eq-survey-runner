# TODO
"""
- Find a way to remove all hardcoding. Can these be held globally in a properties file?

- Get unit tests set up for running of script (e.g. against different JSON, outputs etc)

- Add/amend other team/best practice stuff that's been missed out.

- Will this be run from command line for now? Guard against different inputs.
"""


import json
import os.path
import re
import sys

TEXT_SEPARATOR = "±"
SCHEMA_DIR = "/Users/darrellcox/projects/eq-survey-runner/app/data/"


def is_text_present(text, key):
    return text.get(key) != None and text.get(key) != ''


# Builds and returns a list of translatable text from JSON file
def get_text():

    # Get the JSON file
    with open(file, 'r', encoding="utf8") as jsonData:
      data = json.load(jsonData)

    # Create the list of strings we're going to build up and assign 'header' text first
    # translatable_text = [data['title'], data['description'], data['introduction']['description']]
    translatable_text = [data['title'], data['description']]

    # for value in data['introduction']['information_to_provide']:
    #     translatable_text.append(value)

    # Keys we need to get text for
    keys = [
      'description',
      'guidance',
      'label',
      'title'
    ]

    # Now build up translatable text from the nested dictionaries and lists
    for key in keys: ##

        for group in data['groups']:
            for block in group['blocks']:
                if is_text_present(block, key): ##
                    translatable_text.append(block.get(key))

                for section in block['sections']:
                    if is_text_present(section, key):
                        translatable_text.append(section.get(key))

                    for question in section['questions']:
                        if is_text_present(question, key):
                            translatable_text.append(question.get(key))

                        for answer in question['answers']:
                            if is_text_present(answer, key):
                                translatable_text.append(answer.get(key))

                            if 'validation' in answer:  # Ensure key is available!

                                for value in answer['validation']['messages'].values():
                                    translatable_text.append(value)

    return translatable_text


def sort_text(text_to_sort):
    # Convert to set to remove all duplicates
    unique_text = set(text_to_sort)

    # Convert back to list to sort
    sorted_translatable_text = list(unique_text)
    sorted_translatable_text.sort(reverse=True)

    return sorted_translatable_text


def output_to_file(text_list):
    # Dump the output to a file
    with open('test.txt', 'w', encoding="utf8") as test_file:

        # Output the list - this is just for testing! Please remove after!
        for line in text_list:
            # tester = re.split('({{.+?}})', line, maxsplit=1)
            # print(tester)
            print("%s" % line + TEXT_SEPARATOR + line.upper())

        for line in text_list:
            test_file.write("%s" % line + TEXT_SEPARATOR + line.upper() + "\n")


def usage():
    print()
    print('Usage: python ' + os.path.basename(__file__) + ' <json_schema_file_name>')
    exit(1)


def check_file_exists(file_name):
    if not os.path.isfile(file_name):
        print()
        print('JSON file ' + '\'' + file_name + '\'' + ' not found.')
        exit(2)


# Entry point for entire script for now...
# if len(sys.argv) < 2:
#   usage()     # Incorrect number of args passed in


# file = SCHEMA_DIR + sys.argv[1]
# file = SCHEMA_DIR + '1_0112.json'
file = SCHEMA_DIR + 'census_household.json'
check_file_exists(file)

output_to_file(sort_text(get_text()))
