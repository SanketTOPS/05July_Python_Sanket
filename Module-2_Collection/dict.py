from turtle import st


stdata={'id':1,"name":"nirav","sub":"python"}
"""print(stdata)
print(stdata["name"])
print(stdata.get("sub"))
"""
#print(len(stdata))

#print(stdata.keys())
#print(stdata.values())

"""if 'nirav' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if "nirav" in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

#Key=id and Value=1
#Key=name and Value=nirav
#Key=sub and Value=python
"""
for i,j in stdata.items():
    print(f"Key={i} and Value={j}")"""

#stdata["id"]=2

stdata["city"]="rajkot"
#stdata.pop("sub")
#del stdata["city"]
#del stdata
#stdata.clear()
#print(stdata)

newdict=stdata.copy()
print(newdict)