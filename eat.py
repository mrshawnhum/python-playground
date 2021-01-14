import re

text = "Random phone number is 123-445-6789"

pattern = 'phone'
matches = re.findall('phone', text)
# print (matches)

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
# print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)

print(results.group())