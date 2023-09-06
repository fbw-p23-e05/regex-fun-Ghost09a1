import re

input_string = "Hello123_this_is_valid"

# regex pattern
pattern = r'^[a-zA-Z0-9_]+$'

if re.match(pattern, input_string):
    print("The string contains only valid characters.")
else:
    print("The string contains invalid characters.")
