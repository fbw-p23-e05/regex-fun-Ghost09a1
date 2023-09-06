import re

input_string1 = "acb"
input_string2 = "axxxb"
input_string3 = "abcxyzb"

# regex pattern
pattern = r'^a.*b$'

#  re.match() 
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
