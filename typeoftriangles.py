a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
c=int(input("enter the value for c:"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoselous triangle")
else:
    print("scalen triangle")
