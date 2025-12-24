
# Regex  in pyhton means "Regular Expression" , used to more powerfully for  search , match, extract and replace using patterns instead of using exact wors.
#It helps when we do not know the exact the words, when you need to pattern based macthing as you want to validate inputs like username, email or phone number or CNIC eyc
#
# import re
# pattern = r"^[a-z 0-9]+@+[a-z]"


# email= input("Enter your email")
# if re.match(pattern,email):
#     print("your email is correct :{}".format(email))
# else:
#     print("Wrong Email")

import re

pattern = r"^\w+@\w+\.\w+$"

emails = [
    "ahmed@gmail.com",
    "ahmed@@gmail.com",
    "ahmed gmail.com",
    "ahmed@gmail"
]

for email in emails:
    print(email, "=>", bool(re.match(pattern, email)))