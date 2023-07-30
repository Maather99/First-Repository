import random

secretNum=(random.randint(1,10))
num=0

while(num!= secretNum):
    num=int(input("What is the number? "))
    if(num< secretNum):
        print("Go upper")
        continue
    elif (num> secretNum):
        print("Go lower")
        continue
    else:
        print("Correct answer")
        
        
    
