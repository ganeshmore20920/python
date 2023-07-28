# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
roomlist = input().split()
roomset = set(roomlist)
for ele in list(roomset):
    roomlist.remove(ele)
captainroomno = roomset.difference(set(roomlist)).pop()
print(roomset)
print(roomlist)
print(captainroomno)