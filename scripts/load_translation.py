import json
import ast
from collections import OrderedDict

with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    # data = json.load(jsonData, object_pairs_hook=OrderedDict)

    data = json.load(jsonData)
    print(data)


with open("/Users/liamtoozer/projects/eq-survey-runner/scripts/test.txt", "r") as file:

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
      json_str = json_str.replace(new_list[index][0], new_list[index][1])
    index = index + 1

  print(json_str)

  # Convert string into dictionary, ready for json.dumps()
  # Is this the best alternative to built-in eval()?
  json_str = dict(ast.literal_eval(json_str))



  target_file = open('translated.json', 'w')

  out = json.dumps(json_str, indent=4, separators=(',', ': '))
  target_file.writelines(out)
