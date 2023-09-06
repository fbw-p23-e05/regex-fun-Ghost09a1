import re

input_string = "The Quick brown FOX jumps over the lazy DOG."

# regex pattern 
pattern = r'\b[A-Z][a-z]+\b'

#  re.findall() 
matches = re.findall(pattern, input_string)

if matches:
    print("Sequences of one uppercase letter followed by lowercase letters found:")
    for match in matches:
        print(match)
else:
    print("No sequences of one uppercase letter followed by lowercase letters found.")
