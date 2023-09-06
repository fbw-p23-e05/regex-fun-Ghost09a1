import re

input_string = "World!"
number = 42

# regex pattern 
pattern = r'^'

# replace
result_string = re.sub(pattern, str(number), input_string)

print(result_string)
