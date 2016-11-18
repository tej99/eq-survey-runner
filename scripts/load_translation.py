# TODO
"""
1 - Sort out the loop for string replacement. There's got to be a better way of doing it than this!

2 - Find a way to remove all hardcoding. Can these be held globally in a properties file?

3 - Do we need to worry about ordering of JSON output?

4 - Add/amend other team/best practice stuff that's been missed out.

5 - Will this be run from command line or called from another script for now? Guard against different inputs.
"""

import json
import ast
from collections import OrderedDict

with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    # data = json.load(jsonData, object_pairs_hook=OrderedDict)
    data = json.load(jsonData, object_pairs_hook=OrderedDict)

    # data = json.load(jsonData)
    print(data)


with open("/Users/liamtoozer/projects/eq-survey-runner/scripts/test.txt", "r", encoding="utf8") as file:

  lines = list(file)

  json_str = str(data)

  new_list = []


  # Remove newline characters and split each line into 2 by using a given separator
  # (i.e. ["translatable text] with ["translated text"])
  for line in lines:
      line = line.strip()
      new_list.append(line.split("±"))



  # There's probably a much better way of doing this bit...
  index = 0
  new_string = ''
  for row in new_list:
    if new_list[index][0] in json_str:
      # json_str = json_str.replace(new_list[index][0], new_list[index][1])
      json_str = json_str.replace(new_list[index][0], new_list[index][1])
    index = index + 1

  print(json_str)

  # Convert string into dictionary, ready for json.dumps()
  # Is this the best alternative to built-in eval()? Not sure of an alternative?
  # this does not allow an ordereddict
  # json_str = dict(ast.literal_eval(json_str))
  json_str = OrderedDict(eval(json_str))



  target_file = open('translated_1.json', 'w')

  out = json.dumps(json_str, indent=4, separators=(',', ': '))
  target_file.writelines(out)
