m1=[[1,2,3],[6,3,5]]
m2=[[1,2,3],[6,3,5]]
m3=[]

if len(m1)==len(m2) and len(m1[0])==len(m2[0]) and len(m1[1])==len(m2[1]):
    for i in range(2):
        for j in range(3):
            m3.append(m1[i][j]+m2[i][j])
else:
    print("Error")
            
            
print(m3)