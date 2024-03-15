import re
def numbers_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    else:
        return False
test_cases=[
    "igorkaaristocrat@gmail.com",
    "igorbossgmail.com",
    "igorka_gmail.com"
]
for email in test_cases:
    print(f"{email}: {numbers_email(email)}")