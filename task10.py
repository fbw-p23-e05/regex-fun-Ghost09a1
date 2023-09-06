import re

input_string = "Python is a popular programming language."

# regex pattern
pattern = r'^\w+'

#  re.search() 
match = re.search(pattern, input_string)

if match:
    print("Word at the beginning of the string found:")
    print(match.group())
else:
    print("No word at the beginning of the string found.")
