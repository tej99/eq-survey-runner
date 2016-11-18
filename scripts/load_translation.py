import json
from collections import OrderedDict

with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    # data = json.load(jsonData, object_pairs_hook=OrderedDict)

    data = json.load(jsonData)
    print(data)


with open("/Users/liamtoozer/projects/eq-survey-runner/scripts/test.txt", "r") as file:

  lines = list(file)

  json_str = str(data)

  new_list = []


  # Remove newline characters and split each line into 2 by the separator
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


  # Write out to new json file??? No idea how to do this if we have a string to dict!
  # target_file = open('translated.json', 'w')
  #
  # # json_dump = json.dumps(json_str, indent=4, separators=(',', ': '))
  #
  # jdict = dict(json_str)
  # json_dump = json.dumps(jdict)
  # target_file.write(json_dump)
