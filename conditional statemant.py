marks = int(input("enter marks :"))
if (marks == 100):
    print("outstanding")
elif(marks <= 99 and marks >=90):
    print("superb")
elif(marks <=89 and marks >=80):
    print("A")
else:
    print("B")