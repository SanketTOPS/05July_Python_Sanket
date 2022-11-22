fl=open("test.txt","r+")

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[2])

"""if fl.readable():
    print("Yes...")
else:
    print("Noo")"""

"""for i in fl:
    print(i)"""

fl.write("\nHello Student")