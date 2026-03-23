
# while loop


'''n = int(input("Enter number of terms: "))
sum=0
a = 0
b = 1
i = 1

while i <= n:
    sum+=a
    c = a + b
    a = b
    b = c
    i += 1
print(sum, end=" ")'''

#for loop
n = int(input("Enter number of terms: "))
a=0
b=1
for i in range(2,n):
    c=a+b
    print(c,end='')
    b=a
    c=b

