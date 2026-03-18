num=int(input("enter the number"))
temp=num
rev=0
while temp!=0:
    rem=temp%10
    rev=rev*10+rem
    temp //=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")