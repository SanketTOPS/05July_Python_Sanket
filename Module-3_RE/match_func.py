import re

mystr="Hello Python!"
#mystr=input("Enter Username:")

x=re.match("Python",mystr)
print(x)

if x:
    print("Your Username in valid!")
else:
    print("Error!Plz try again...")
