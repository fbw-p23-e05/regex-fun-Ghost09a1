import re

input_string1 = "abb"
input_string2 = "abbb"
input_string3 = "abbbb"
input_string4 = "ab"

# regex pattern
pattern = r'^a(bb|bbb)?$'

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

if re.match(pattern, input_string4):
    print(f"'{input_string4}' matches the pattern.")
else:
    print(f"'{input_string4}' does not match the pattern.")
