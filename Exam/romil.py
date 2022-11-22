fl=open("text.txt", "a")
name=input("Enter the name:")
id=int(input("Enter id:"))
subject=(input("Enter subject:"))


fl.write(f"Name:{name}\n")
fl.write(f"ID:{id}\n")
fl.write(f"Enter subject:{subject}\n")




