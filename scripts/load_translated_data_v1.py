import json

with open('/Users/darrellcox/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData)
    jsonData.close()
    # print(data)

text_file = open('/Users/darrellcox/projects/eq-survey-runner/scripts/test.txt', 'r', encoding="utf8")
list1 = text_file.readlines()


def print_all_translatable():
    for value in list1:
        print("%s" % value)

print_all_translatable()



# content = data.read()
# data.seek(0)
# content.replace("Monthly Business Survey", "MONTHLY BUSINESS SURVEY")
# data.write(content)
# print(content)

#trial_replace()

