num=int(input("enter a no.: "))
sum=0
temp=num
while temp!=0:
    rem=temp%10
    sum+=rem
    temp//=10

print(sum)