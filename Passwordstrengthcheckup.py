password = input("Enter password: ")
upper = 0
lower = 0
digit = 0
special = 0
for ch in password:
    if ch.isupper():
        upper = 1
    elif ch.islower():
        lower = 1
    elif ch.isdigit():
        digit = 1
    else:
        special = 1
if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
