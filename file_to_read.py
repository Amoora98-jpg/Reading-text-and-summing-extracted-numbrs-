import os
import sys
import re
# get the directory of your script
script_dir = os.path.dirname(os.path.abspath(__file__))
# creating full path to the file
file_path = os.path.join(script_dir, "regex_sum_2242260.txt")
# try opening the file
try:
    with open(file_path, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
list_of_digits = re.findall('[0-9]+', content)
sum_of_digits = sum([int(num) for num in list_of_digits])
print(sum_of_digits)
