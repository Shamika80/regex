import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key_to_extract = "Occupation"  

pattern = r"(?P<key>\w+):\s+(?P<value>.+)"

matches = re.findall(pattern, text)

for match in matches:
    if match["key"] == key_to_extract:
        value = match["value"]
        print(f"Value for '{key_to_extract}': {value}")
        break  

else:
    print(f"Key '{key_to_extract}' not found in the text.")