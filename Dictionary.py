contacts={"Maather":1,"Thuraya":2,"Batoul":3}

conn=dict(contacts)
print(conn)
print()


print(contacts["Maather"])
print()


if "Sana" in contacts:
    print(contacts[" Sana"])
else:
    print("Not found")
print()


#to add new key
contacts["Sana"]=4
print(contacts)
print()


#to delete new key
contacts.pop("Thuraya")
print(contacts)
print()


#to print the key with value
for key in contacts:
    print(key, contacts[key])
print()


for item in contacts.items():
    print(item[0], item[1])
    
