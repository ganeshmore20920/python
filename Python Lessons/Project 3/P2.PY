n = int(input())
student = []
for i in range(2*n):
    student.append(input().split())
grades = {}
for j in range(0,len(student),2):
    grades[student[j][0]] = float(student[j+1][0])
result = []
num = sorted(set(grades.values())[1])
for pup in grades.keys():
    if grades[pup] == num:
        result.append(pup)
    