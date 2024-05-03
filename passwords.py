import random
import string

strongpass = []

strongpass.append(list(string.ascii_lowercase)[random.randint(0,len(list(string.ascii_lowercase)))-1])
strongpass.append(list(string.ascii_uppercase)[random.randint(0,len(list(string.ascii_uppercase)))-1])
strongpass.append(random.randint(0,9))
strongpass.append(list(string.punctuation)[random.randint(0,len(list(string.punctuation)))-1])

charlist = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

for x in range(0,random.randint(4,12)):
    strongpass.append(charlist[random.randint(0,len(charlist))-1])

print(*strongpass, sep="")

flag = False
count = 0
while flag != True:
    userpass = input("""Your password must contain at least:
8 characters
1 lowercase
1 uppercase
1 digit
1 special character
Enter here: """)
    if not(len(userpass) >= 8):
        print("Password requires at least 8 characters.")
        continue
    if not(any(x in string.ascii_lowercase for x in userpass)):
        print("Password requires at least 1 lowercase character.")
        continue
    if not(any(y in string.ascii_uppercase for y in userpass)):
        print("Password requires at least 1 uppercase character.")
        continue
    if not(any(z in string.digits for z in userpass)):
        print("Passwod requires at least 1 digit.")
        continue
    if not(any(a in string.punctuation for a in userpass)):
        print("Password requires at least 1 special character.")
        continue
    print("Password accepted.")
    flag = True
