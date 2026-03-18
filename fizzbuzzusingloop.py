'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("fizzbuzz",end=' ')
    elif(i%3==0):
        print("fizz",end=' ')
    elif(i%5==0):
        print("buzz",end=' ')
    else :
        print(i,end=' ')'''


n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(i%7==0 and i%9==0):
        print("fizzbuzz",end=' ')
    elif(i%7==0):
        print("fizz",end=' ')
    elif(i%9==0):
        print("buzz",end=' ')
    else :
        print(i,end=' ')
