Number = input("Number of item: ")
Array = input("Enter items: ")
for i in range(0, len(Array)):
    for j in range(i+1, len(Array)):
        for x in range(j+1, len(Array)):
            if(Array[i] == Array[j] == Array[x]):
                print(Array[x]);