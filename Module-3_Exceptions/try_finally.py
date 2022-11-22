try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
except Exception as e:
    print(e)
else:
    print("This is Finally Block.")