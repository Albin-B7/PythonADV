# file_path = "example"
# file = open(file_path)
#
#
# content = file.read()
# print(content)
#
# file.close

import os

with open('example', 'r') as  file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()

with open("example", 'w') as file:
    file.write("Amiri nuk po shrkun kod po rrin ne telefon")

lines = ["Amiri edhe Noart shkruajn shum shpejt\n", "Erioni dhe Germaniumi hajn shum haribo"]

with open("example", 'w') as file:
    file.writelines(lines)