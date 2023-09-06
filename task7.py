import re

input_string = "hello_world is_a_sequence of_lowercase_letters_like_this."

# regex pattern 
pattern = r'\b[a-z]+_[a-z]+\b'

# re.findall() 
matches = re.findall(pattern, input_string)

if matches:
    print("Sequences of lowercase letters joined by an underscore found:")
    for match in matches:
        print(match)
else:
    print("No sequences of lowercase letters joined by an underscore found.")
