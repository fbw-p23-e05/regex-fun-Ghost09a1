import re

input_string1 = "Hello123"
input_string2 = "Python@2021"
input_string3 = "OpenAI-GPT3"

#regex pattern
pattern = r'^[a-zA-Z0-9]+$'

#  re.match()
if re.match(pattern, input_string1):
    print(f"'{input_string1}' contains only valid characters.")
else:
    print(f"'{input_string1}' contains invalid characters.")

if re.match(pattern, input_string2):
    print(f"'{input_string2}' contains only valid characters.")
else:
    print(f"'{input_string2}' contains invalid characters.")

if re.match(pattern, input_string3):
    print(f"'{input_string3}' contains only valid characters.")
else:
    print(f"'{input_string3}' contains invalid characters.")
