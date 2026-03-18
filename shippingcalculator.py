'''weight=int(input("enter the weight: "))
express=input("Do you want express: ").lower
if weight<2 and True:
    print('$10')
elif weight<2 and False:
    print('$5')
elif weight<10 and True:
    print('$15')
elif weight<10 and False:
    print('$10')
elif weight>10 and True:
    print('$25')
else:
    print('$20')'''

weight=int(input("enter the weight: "))
express=input("Do you want express: ")
if weight<2:
    total=5
elif weight<10:
    total=10
else:
    total=20
if express=="true":
    total+=5
print(express)
print(total)
