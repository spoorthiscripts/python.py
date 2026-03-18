marks= int(input("Enter the marks"))
if 90 <= marks <= 100 :
    print("Grade A")
elif 75 <= marks < 90:
    print("Grade B")
elif 60 <= marks < 75:
    print("Grade C")
elif 40 <= marks < 60:
     print("Grade D")
else:
    print("Grade F")