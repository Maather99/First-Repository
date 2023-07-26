Year = int (input ("Eter any year to check if it is a leap year: "))
if (Year %4) == 0:
    if(Year %100) == 0:
    
        if (Year %400) == 0:
           print("The given year is a leap year")
        else:
           print("It is not a leap year")
           
    else:
        print("It is not a leap year")
else:
    print("It is not a leap year")