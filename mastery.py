import re

text = "Contact emails are: john.doe@example.com and jane.doe@username.co.uk."

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)