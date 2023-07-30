string=(input("Enter :"))
uppercase=0
for char in string:
    if char.isupper():
        uppercase=uppercase+1
print(uppercase)