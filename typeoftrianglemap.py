a,b,c = map(int,input().split())
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoselous triangle")
else:
    print("scalen triangle")