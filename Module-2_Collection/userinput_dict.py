mydict={}

n=int(input("Enter the number of pairs:"))

for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    mydict[key]=value

print(mydict)