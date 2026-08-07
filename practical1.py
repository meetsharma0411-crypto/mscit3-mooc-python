roll_no =int(input("Enter Student Roll_No : "))
name =input("Enter Student Name    : ")
age = int(input("Enter Student Age     : "))

marks1 = 75
marks2 = 68
marks3 = 80
total = marks1 + marks2 + marks3
percentage = total / 3
passed = (marks1 >= 40) and (marks2 >= 40) and (marks3 >= 40)

print("===== Student Information =====")
print("Roll No.   :", roll_no)
print("Name       :", name)
print("Age        :", age)
print("\nMarks")
print("Math    1 :", marks1)
print("English 2 :", marks2)
print("Hindi   3 :", marks3)
print("\nTotal Marks      :", total)  
print("Percentage       : {:.2f}%".format(percentage))

if passed:
    print("Result : PASS")
else:
    print("Result : FAIL")