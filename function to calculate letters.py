s=input("Enter: ").upper()
v=("a,u,o,i,e").upper()

def check_letters(string):
    counter=0
    for i in string:
        if (i in v):
            counter +=1
    return counter

print(check_letters(s))
    