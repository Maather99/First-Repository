values=[]
print("Please enter values, 0 to quit: ")
user= input(" ")
while user.upper()!="Q":
    values.append(float(user))
    user= input("Please enter values, 0 to quit:")
print(values)