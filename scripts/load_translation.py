

text_file = open('/Users/darrellcox/projects/eq-survey-runner/scripts/test.txt', 'r', encoding="utf8")
list1 = text_file.readlines()

for value in list1:
    print("%s" % value)
