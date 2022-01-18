import  re

with open('assets/potential-contacts.txt', 'r') as f:
    text = f.read().replace('\n', '')

reg_phone_numbers = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)

reg_emails = re.compile(r'''([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

phone_numbers = []
all_emails = []

for i in reg_phone_numbers.findall(text):
    phone_num = '-'.join([i[1], i[3], i[5]])
    phone_num = re.sub(r'[(|)]','', phone_num)
    if phone_num not in phone_numbers:
        phone_numbers.append(phone_num)
for j in reg_emails.findall(text):
    if j[0] not in all_emails:
        all_emails.append(j[0])

phone_numbers.sort()
all_emails.sort()

with open("./assets/phone_numbers.txt","w+") as f:
    for element in phone_numbers:
     f.write(element + "\n")

with open("./assets/all_emails.txt","w+") as f:
    for element in all_emails:
     f.write(element + "\n")

