hour1= (input("Enter firs time:"))
minute1= (input("Enter minuts:"))
hour2= (input("Enter second time:"))
minute2= (input("Enter minuts:"))
firstHour=(hour1+":"+minute1)
secondHours=(hour2+":"+minute2)
if(hour1==hour2):
    if(minute1>minute2):
        print(firstHour+ " is next")
    elif(minute1<minute2):
        print(secondHours+ " is next")      
elif(hour1>hour2):
    print(firstHour+" is next")
else:
    print(secondHours+" is next")








