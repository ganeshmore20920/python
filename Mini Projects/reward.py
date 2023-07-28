# input2 = input()
# reward = 0;
# for i in range(len(input2)):
#     if(int(input2[i])%2 == 1):
#         reward += int(input2[i])
# print("input : " + input2)
# print("output : " + reward)


# s = "aAkliP"
# print(ord("a")-ord("A")+ord("k")+ord("l")+ord("i")-ord("P"))



asc = input("input : ")
listing = []
for i in range(len(asc)):
    listing.append(ord(asc[i]))
sorting = sorted(listing)
print("output : ",end="")
print(sorting[0] + sorting[len(sorting)-1])