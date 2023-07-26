x = int(input("Enter size of storage: "))
n = int(input("Enter number of files: "))
y = int(input("Enter size of files: "))
Full_size= n*y
if (Full_size<=x):
    print("You can store")
else:
    print("You can not store")