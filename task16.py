import re

ip_address = "192.001.010.003"

#regex pattern  IP address
pattern = r'\b0+(\d+)\b'

# clean IP address
cleaned_ip = re.sub(pattern, r'\1', ip_address)

print(cleaned_ip)
