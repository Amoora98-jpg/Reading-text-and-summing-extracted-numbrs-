import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "romeo.txt")
with open(file_path,"r") as file:
    content = file.read()
    words = content.split()
    print(words)




