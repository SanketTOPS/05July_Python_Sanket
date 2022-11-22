fl=open("test.txt","a")

id=input("Enter ID:")
name=input("Enter Name:")
sub=input("Enter Subject:")

fl.write(f"ID:{id}\n")
fl.write(f"Name:{name}\n")
fl.write(f"Subject:{sub}\n")
fl.write(f"---------------------\n")
