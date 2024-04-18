import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@anotherdomain.com"
domain_to_exclude = "exclude.com"

emails = re.findall(fr"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(?<!\.{domain_to_exclude})\.[a-zA-Z]{2,}\b", text)

print(emails)