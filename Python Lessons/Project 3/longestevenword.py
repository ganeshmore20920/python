inp = input()
def longestEvenWord(sentence):
    ex_list = sentence.split(" ")
    ind = []
    leng = len(ex_list)
    for i in range(leng):
        ind.append(len(ex_list[i]))
    ind2 = sorted(ind)
    index_value = 0
    for j in range(leng-1):
        if(ind2[leng-1-j]%2 == 0):
            index_value = ind2[leng-1]
            break
    ret = ""
    for k in range(leng):
        if(ind[k] == index_value):
            ret = ret + ex_list[k]
            break
    return ret
            

print(longestEvenWord(inp))