import re

password = str(input("Enter string to test: "))
if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
    print("match")
else:
    print("not match")
