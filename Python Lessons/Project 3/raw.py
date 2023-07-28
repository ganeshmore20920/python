inp = input()
ex_list = inp.split(" ")
ind = []
for i in range(len(ex_list)):
    ind.append(len(ex_list[i]))
ind2 = ind
ind2 = sorted(ind2)
leng = len(ind2)
index_value = 0
for j in range(len(ex_list)-1):
    if(ind2[leng-1-j]%2 == 0):
        index_value = ind2[len(ind2) - 1]
        break
print(index_value)
for k in range(leng):
    if(ind[k] == index_value):
        print(ex_list[k])
        break