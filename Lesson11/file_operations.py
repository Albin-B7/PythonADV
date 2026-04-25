# file_path = "example"
# file = open(file_path)
#
#
# content = file.read()
# print(content)
#
# file.close

import os

from tensorflow.python.framework.test_ops import binary

with open('example', 'r') as  file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()

with open("example", 'w') as file:
    file.write("Amiri nuk po shrkun kod po rrin ne telefon")

lines = ["Amiri edhe Noart shkruajn shum shpejt\n", "Erioni dhe Germaniumi hajn shum haribo"]

with open("example", 'w') as file:
    file.writelines(lines)

with open("example", 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)

if os.path.exists('example'):
    print("File exist")

with open ('example', 'a') as file:
    file.write('\nNew data appended')

data = b'This is some binary data'
with open('example.bin', 'wb') as file:
    file.write(data)

with open('example.bin', 'rb')as binary_file:
    data = binary_file.read()
    print(data)