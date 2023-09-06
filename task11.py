import re

input_string = "Hello, world! This is a test. The word 'Python'."

# regex pattern
pattern = r'\b\w+[.,;!?]*$'

# re.search() 
match = re.search(pattern, input_string)

if match:
    print("Word at the end of the string with optional punctuation found:")
    print(match.group())
else:
    print("No word at the end of the string with optional punctuation found.")
