Dict1={}
Len=int(input("enter the how many student data upload : "))
for i in range(Len):
    Std_name = input("Student name  : ")
    Std_mark = int(input("enter marks   : "))
    Dict1[Std_name]=Std_mark
    
    
print("\n")
list_mark=list(Dict1.values())
Tuple_mark=tuple(Dict1.values())
print("Data Types of Data")
print("list Type Marks      : ",list_mark)
print("Tuple Type Marks     : ",Tuple_mark)
print("Dictionary Type Data : -",Dict1)

avg = sum(list_mark)/len(list_mark)
print("\n")
print("Highest Marks        : ",max(list_mark))
print("Lowest Marks         : ",min(list_mark))
print("Average Marks        : ",avg)
list_avg=[]

for i in range(len(list_mark)):
    if list_mark[i] > avg:
        list_avg.append(list_mark[i])

print("\n")
print("List Of The Above Avarange Marks",list_avg)
Set_mark=set(list_mark)
print("USe Set DataType Marks List : ",Set_mark )        
        