import numpy as np

subject=("java","python","c","os","ml")
all_marks=[]
stu_name=[]
irn=input("enter batch like this Batch-2026-Computer_Science :-")

de=irn.split("-",2)[2]
bath=irn.split("-",1)[1]


for i in range(2):
    stu=input("student name ")
    stu_name.append(stu)
    stu_mar=[]
    for j in range(2):
        mar=int(input(f"student name{stu} roll :{i+1} enter mark :{subject[j]} "))
        stu_mar.append(mar)
    #all_marks=np.array(all_marks,stu_mar, axis=0)
    all_marks.append(stu_mar)

#print(stu_name)
#print(all_marks)

all_marks=np.array(all_marks)
#print(all_marks)
print("all stdent marks\n")
student_total_mark=np.sum(all_marks,axis=1)
print("subject wise all subject total\n")
subject_total=np.sum(all_marks,axis=0)
student_per=[] 

for i in range(len(student_total_mark)):
    stu_per=student_total_mark[i]/2
    student_per.append(stu_per)
print("all student subject total",student_total_mark)
highest_index = np.argmax(student_total_mark)
print("student with highest total marks:", stu_name[highest_index])
subject_marks_avg=np.mean(all_marks,axis=0)
print("subject mark avagange",subject_marks_avg)
print("student persentage",student_per)
highest_mar=np.max(student_total_mark)
lowest_mar=np.min(student_total_mark)
average_mar=np.mean(student_per)
print("highest marks in class",highest_mar)
print("lowest marks in class",lowest_mar)
student_per_avg=np.mean(student_per)

marks_ave_high=np.max(np.mean(all_marks,axis=0))
marks_ave_low=np.min(np.mean(all_marks,axis=0))

print(np.mean(all_marks,axis=0))
marks_ave_high_index=np.argmax(np.mean(all_marks,axis=0))
marks_ave_low_index=np.argmin(np.mean(all_marks,axis=0))
print(f"highest marks in subject {subject[marks_ave_high_index]} with average marks {marks_ave_high}")
print(f"lowest marks in subject {subject[marks_ave_low_index]} with average marks {marks_ave_low}")
h=all_marks[:3,-2:]
print("printing first 3 student marks in first 2 subject",h)
print('\n')

print("Student Performance Analytics")

search_subject = input("\nEnter subject to search: ").strip()

if search_subject in subject:

    subject_index = subject.index(search_subject)

    print(f"{search_subject} exists in subject tuple ")

else:
    print("Subject not found.")
stud_index=[]
stuf_index=[]
for i in range(len(stu_name)):
    if student_per[i] >  85:
        stud_index.append(stu_name[i])
    elif student_per[i] < 40:
        stuf_index.append(stu_name[i])
        

print("students with more than 85% marks",stud_index)
print("students with less than 40% marks",stuf_index)
stuave_index=[]
for i in range(len(stu_name)):
     if student_per[i] > average_mar:
         stuave_index.append(stu_name[i])

print("students with more than average marks",stuave_index)

reverse_stu_name=stu_name[::-1]
print("reverse student name",reverse_stu_name)

alp=sorted(stu_name)

print("alphabetically sorted student names",alp)

print("-------------------")
print("Summary Report")
print("-------------------")

print("department:", de)
print("batch:", bath)
print("total students:", len(stu_name))
print("avarange percetage of class:", student_per_avg)
print("highest score student:",stu_name[highest_index])
print("lowest score student:",stu_name[np.argmin(student_total_mark)])

marks_ave_high_index = np.argmax(subject_marks_avg)
print(f"subject with highest average marks: {subject[marks_ave_high_index]} with average marks {marks_ave_high}")
marks_ave_low_index = np.argmin(subject_marks_avg)  
print(f"subject with lowest average marks: {subject[marks_ave_low_index]} with average marks {marks_ave_low}")

print("number of distinction students:", len(stud_index))
print("number of failed students:", len(stuf_index))