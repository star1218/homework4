# import re  #3
# def numbers_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern,email):
#         return True
#     else:
#         return False
# test_cases=[
#     "igorkaaristocrat@gmail.com",
#     "igorbossgmail.com",
#     "igorka_gmail.com"
# ]
# for email in test_cases:
#     print(f"{email}: {numbers_email(email)}")

# import re  #2
# def numbers_phone(phone_number):
#     pattern=r'^\+?[0-9]{7,15}$'
#     if re.match(pattern,phone_number):
#         return True
#     else:
#         return False
# test_cases=[
#     "+380985881806",
#     "380683740047",
#     "0934243296",
#     "98321",
#     "12345567785323455675"
# ]
# for phone in test_cases:
#     print(f"{phone}:{numbers_phone(phone)}")