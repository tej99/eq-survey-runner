import json
import re

with open('/Users/darrellcox/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData)
    jsonData.close()


text_file = open('/Users/darrellcox/projects/eq-survey-runner/scripts/test.txt', 'r', encoding="utf8")
list1 = text_file.readlines()
# list1.split("|")

jsonString = str(data)

def choose_awkward_characters():
    s = '{{exercise.start_date|pretty_date}}'
    result = re.search('{{(.*)}}', s)
    print(result.group(1))


def print_all_translatable():
    for value in list1:
        new_lists = value.split("±")
        #sprint(new_lists)
        print("%s" % value.split("±"))
        # if json data equals whatever is in new_lists[0] print new_lists[1]
        if new_lists[0:] == jsonString:
            print(new_lists[1])

#        for row in new_list:
#           if json_str == new_list[row][0]:
#               json_str.replace(new_list[row][0], new_list[row][1])

#print_all_translatable()
#choose_awkward_characters()
print_all_translatable()


# content = data.read()
# data.seek(0)
# content.replace("Monthly Business Survey", "MONTHLY BUSINESS SURVEY")
# data.write(content)
# print(content)

#trial_replace()

