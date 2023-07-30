from math import pi


def sequre(length):
    s=(length**2)
    return s      
def circle(radius):
    c=((pi)*radius**2)
    return c
def rectangle(rLength, rWeight):
    r=(rLength*rWeight)
    return r 
def cylinder(halhTheBase, cLength):
    cy=((2*(pi)*halhTheBase)* (cLength))
    return cy
def tringle(Height, Length):
    t=(0.5*Height*Length)
    return t



n=1
while(n==1):
    txt=(input("Select number(1, 2, 3, 4, 5): "))
    if not(txt == "quit"):
     txt=int(txt)
     if (txt==1):
        l=float(input("What is the length of sequar? "))
        print(sequre(l))
     elif(txt==2):
         r=float(input("What is the radius of circle? "))
         print(circle(r))
    

     elif(txt==3):
         l=float(input("What is the length of rectangle? "))
         w=float(input("What is the weight of rectangle? "))
         print(rectangle(l, w))
    
    
     elif(txt==4):
         h=float(input("What is the halh the base of cylinder? "))
         l=float(input("What is the length of cylinder? "))
         print(cylinder(h,l))
        
    
     else:
         lt=float(input("What is the length of tringle? "))
         ht=float(input("What is the height of tringle? "))
         print(tringle(lt, ht))
         
         
    else:
        break


    
    
