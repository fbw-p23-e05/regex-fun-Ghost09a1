import re

input_string1 = "ab"
input_string2 = "a"
input_string3 = "abb"
input_string4 = "ac"

# regex pattern
pattern = r'^ab?$'

# re.match() 
if re.match(pattern, input_string1):
    print(f"'{input_string1}' matches the pattern.")
else:
    print(f"'{input_string1}' does not match the pattern.")

if re.match(pattern, input_string2):
    print(f"'{input_string2}' matches the pattern.")
else:
    print(f"'{input_string2}' does not match the pattern.")

if re.match(pattern, input_string3):
    print(f"'{input_string3}' matches the pattern.")
else:
    print(f"'{input_string3}' does not match the pattern.")

if re.match(pattern, input_string4):
    print(f"'{input_string4}' matches the pattern.")
else:
    print(f"'{input_string4}' does not match the pattern.")
