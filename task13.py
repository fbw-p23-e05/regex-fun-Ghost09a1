import re

input_string = "This is a test string with words like pizza, jazz, and buzzwords."

# regex pattern
pattern = r'\b\w*z\w*\b'

#  re.findall()
matches = re.findall(pattern, input_string)

if matches:
    print("Words containing 'z', not at the start or end, found:")
    for match in matches:
        print(match)
else:
    print("No words containing 'z', not at the start or end, found.")
