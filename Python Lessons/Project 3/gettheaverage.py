n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = list(student_marks.items())
k = []
for j in range(n):
    if(query_name == marks[j][0]):
        k.append(marks[j][1])
result = 0
for pup in range(3):
    result = result + k[0][pup]
a = result/3
print("{0:.2f}".format(a))