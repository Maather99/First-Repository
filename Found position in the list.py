list=[10, 20, 30, 90]
found= False
pos=0
while pos<len(list) and not found:
    if list[pos] == 90:
        found=True
    else:
        pos+=1
        
if found:
    print("position founded")
else:
    print("position not founded")