def readDate():
    print("Enter : ")
    month= input(" Month ")
    day= input(" day ")
    year= input(" Year ")
    return (month, day, year)


date=readDate()
print(date)