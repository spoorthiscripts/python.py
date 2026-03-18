'''weight=float(input("Enter the weight: "))
height=float(input("enter the height: "))
bim=weight/(height**2)
if bim>=30:
    print("Obese")
elif 25 <= bim <30:
    print("overweight")
elif 18.5 <= bim <25:
    print("normal")
elif bim<18.5:
    print("under weight")'''



weight,height=map(float,input("enter the weight and height").split())
bim=weight/(height**2)
if bim<18.5:
    print("under weight")
elif bim <25 :
    print("normal")
elif bim <30:
    print("over weight")
else:
    print("obse")


