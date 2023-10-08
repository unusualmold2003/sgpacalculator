import numpy as np

subjects = int(input("Enter number of subjects: "))

l_grade = []
l_marks = []
l_credits = []
l_sname = []

def marks_input():
    global l_grade, l_marks, l_credits, l_sname
    subject_name = input("\nEnter Subject Name: ")
    l_sname.append(subject_name)
    marks = int(input("Enter the marks: "))
    l_marks.append(marks)
    grade = 0
    if marks >= 90 and marks <= 100:
        grade = 10
    elif marks >= 80 and marks <= 89:
        grade = 9
    elif marks >= 70 and marks <= 79:
        grade = 8
    elif marks >= 60 and marks <= 69:
        grade = 7
    elif marks >= 55 and marks <= 59:
        grade = 6
    elif marks >= 50 and marks <= 54:
        grade = 5
    elif marks >= 40 and marks <= 49:
        grade = 4
    l_grade.append(grade)
    credits = int(input("Enter the no of credits: "))
    l_credits.append(credits)

for i in range(subjects):
    marks_input()

for j in range(subjects):
    print("Subject: {} Marks: {} Grade Point: {} Credits: {}".format(l_sname[j], l_marks[j], l_grade[j], l_credits[j]))

marks = np.array(l_marks)
print("Total percentage is:", (marks.sum() / (100 * subjects)) * 100)

def sgpa_calc():
    arr = np.array(l_credits)
    sgpa = 0
    for i in range(subjects):
        sgpa += (l_grade[i] * l_credits[i])
    return sgpa / arr.sum()

print("Total SGPA is:", sgpa_calc())