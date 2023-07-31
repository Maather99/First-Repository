Weight= float(input("Enter your weight: "))
height= float(input("Enter your height: "))
Height= height/2
BMI=(Weight/(Height**2))
if(BMI<18.5):
    print("underweight")
elif(18.5 <= BMI <= 25.0):
    print("Normal")
elif(25.0 <= BMI <= 30.0):
    print("Overweight")
elif(30.0<= BMI):
    print("Obese")
