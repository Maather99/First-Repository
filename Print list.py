list=[23, 54, 76, 12, 90]
for i in range(len(list)):
    if i ==len(list)-1:
        print(list[i])
    else:
        print(list[i], "|", end=" ")