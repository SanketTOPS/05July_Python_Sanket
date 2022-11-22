import re

mystr="This is Python!"
#mystr=input("Enter Username:")

x=re.search("is",mystr)
print(x)

if x:
    print("Your Username in valid!")
else:
    print("Error!Plz try again...")
