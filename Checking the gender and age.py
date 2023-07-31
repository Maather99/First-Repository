Gender= (input("Enter your gender(F or M): ")).upper()
if(Gender == "F"):
    age = int(input("Enter your age: "))
    if(30>=age>=18):
        print("Accepted")
    else:
        print("Rejected")
else:
    print("Accept only female")
