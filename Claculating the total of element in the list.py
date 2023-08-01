listscore=[50,88,90,75]

def studentAverage(score):
    total=0
    average=0
    for i in range(len(score)):
        total+=score[i]
    average=(total/len(score))
    return average

print(studentAverage(listscore))

   
    