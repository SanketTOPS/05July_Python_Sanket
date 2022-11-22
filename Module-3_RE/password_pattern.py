import re

pas=input("Enter Password:")
#cpas=input("Enter Confirm Password:")

pas_pattern='[A-Z._#@$-?]+[a-z._#@$-?]+[0-9._#@$-?]'

x=re.findall(pas_pattern,pas)

if x:
    print("Password is valid!")
else:
    print('Error!Invalid Password')