

# def get_all_values(d, depth):
#   if depth == 1:
#     for i in d.values():
#       yield i
#   else:
#     for v in d.values():
#       if isinstance(v, dict):
#         for i in d.values(v, depth - 1):
#           yield i


# for value in list1:
#     print(value),

  #
  # contents = file.read()
  #
  #
  # print(contents)



# When finished, get rid of everything between these characters!!!
#!!!

import json

# def get_all_values(d, depth):
#   if depth == 1:
#     for i in d.values():
#       print(i)
#   else:
#     for v in d.values():
#       if isinstance(v, dict):
#         for i in get_all_values(v, depth - 1):
#           print(i)
#
#
with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData)

    # get_all_values(data, 0)
    # get_all_values(data, len(data))








#     data["mime_type"] = 'something/test'
#
#     jsonData.seek(0)
#
#     target_file = open('small_new.json', 'w')
#
#     json_dump = json.dumps(data, indent=4, separators=(',', ': '))
#
#     target_file.write(json_dump)
#
#     #json_dump = json.dumps(data, indent=4, separators=(',', ': '))
#
# #with open("file.txt", "w") as att_file:
# #    att_file.write(data)


    # with open('data.json', 'w') as f:
    #     json.dump(data, f)

# Reading data back

#!!!



"""
- Get a list of each line from the file to translate.
- Search through the JSON file (dict) for any strings which match the left side of text from the file.
- If a matching string is found, replace it with the right side of the text from the file.
"""

with open("/Users/liamtoozer/projects/eq-survey-runner/scripts/test.txt", "r") as file:

    lines = list(file)



    # for line in lines:
    #     # print(line)
    #     new_lists = line.split("|")
    #     # print(new_lists)
    #     print("%s" % line.split("|"))
    #     # if json data equals whatever is in new_lists[0] print new_lists[1]
    #     if new_lists[0] == 'RSI Description':
    #         print(new_lists[1])

    json_str = str(data)
    new_list = []



    for line in lines:
        # print(line)
        # new_lists = line.split("|")
        new_list.append(line.split("±"))
        # print(new_lists)
        # print("%s" % line.split("|"))
        # if json data equals whatever is in new_lists[0] print new_lists[1]
        # if new_lists[0] == 'RSI Description':
        #     print(new_lists[1])

    print(new_list)

    # print(json_str)
    # print(new_list[31][0])
    # print(json_str.replace(new_list[31][0], str(new_list[31][0]).upper()))

    index = 0
    new_string = ''
    for row in new_list:
      if new_list[index][0] in json_str:
        json_str = json_str.replace(new_list[index][0], str(new_list[index][0]).upper())
      index = index + 1

    print(json_str)


    # for i, j in new_list:
    #     print(j)

    # for i, j in new_list:
    #   print(i)

    # for i in new_list:
    #   # print(json_str.replace(new_list[0][0], new_list[0][1]))
    #   print(json_str.replace(new_list[i][0], new_list[i][1]))



    # for line in new_lines:
    #     # line.replace(line[0], line[1])
    #     # replaced = str(line).replace(line[0], line[1])
    #     # print(replaced)
    #     old = line[0]
    #     new = line[1]
    #     print(old, new)






    # print(*lines)
    # print(lines[0])








# for value in list1:
#     print(value),

  #
  # contents = file.read()
  #
  #
  # print(contents)



