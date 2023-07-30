import math
n_side=float(input("Enter number of side: "))
l_side=float(input("Enter number of side: "))

def area(n, side):
    pi=3.14
    a=(n*(side)**2)/(4*(math.tan(pi/n)))
    return a
print(area(n_side, l_side))