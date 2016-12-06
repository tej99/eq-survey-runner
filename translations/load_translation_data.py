# TODO
"""
- Loop through and replace text in deserialised json instead of replacing values in string.
- Ignore any text between '<' and '>' and '{' and '}'.
- Sort out the loop for string replacement. There's got to be a better way of doing it than this!
- Find a way to remove all hardcoding. Can these be held globally in a properties file?
- Do we need to worry about ordering of JSON output?
- Add/amend other team/best practice stuff that's been missed out.
- Will this be run from command line or called from another script for now? Guard against different inputs.
"""

import json
# import ast
from collections import OrderedDict

TEXT_SEPARATOR = "±"
SCHEMA_DIR = "/Users/darrellcox/projects/eq-survey-runner/app/data/"
SCRIPTS_DIR = "/Users/darrellcox/projects/eq-survey-runner/translations/"
TEXT_TO_TRANSLATE = 0
TRANSLATED_TEXT = 1

with open(SCHEMA_DIR + "census_household.json", 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData, object_pairs_hook=OrderedDict)

with open(SCRIPTS_DIR + "census_household_translate.txt", "r", encoding="utf8") as file:
    lines = list(file)

    json_str = str(data)

    new_list = []

    # Remove newline characters and split each line into 2 by using a given separator
    # (i.e. ["text_to_translate] with ["translated text"])
    for line in lines:
        line = line.strip()

        # Ignore anything between {{ and }} here before appending??
        new_list.append(line.split(TEXT_SEPARATOR))

    # There's probably a much better way of doing this bit...
    index = 0
    for row in new_list:
        print(row)

        if new_list[index][TEXT_TO_TRANSLATE] in json_str:
            json_str = json_str.replace(new_list[index][TEXT_TO_TRANSLATE], new_list[index][TRANSLATED_TEXT])
        index += 1

    print(json_str)

    # Convert string into dictionary, ready for json.dumps()
    # Is this the best alternative to built-in eval()? Not sure of an alternative?
    # this does not allow an ordereddict
    # json_str = dict(ast.literal_eval(json_str))
    json_str = OrderedDict(eval(json_str))

    target_file = open(SCHEMA_DIR + 'census_household_cy.json', 'w')

    out = json.dumps(json_str, indent=4, ensure_ascii=False, separators=(', ', ': '))
    target_file.writelines(out)
