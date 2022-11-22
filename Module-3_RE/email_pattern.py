import re

#sanket.chauhan@gmail.com

email=input("Enter an email:")
email_pattern='^[a-z0-9._]+@+[a-z]+[\.]+[a-z]{2,}$'

x=re.findall(email_pattern,email)

if x:
    print("Email is valid!")
else:
    print("Error!Invalid Email.")