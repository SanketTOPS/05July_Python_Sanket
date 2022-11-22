import re

mystr="This is Python!"
#mystr=input("Enter Username:")

x=re.findall("is",mystr)
print(x)

if x:
    print("Your Username in valid!")
else:
    print("Error!Plz try again...")
