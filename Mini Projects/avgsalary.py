salary = [2000,3000,40000,1000]
salary2 = sorted(salary)[1:(len(salary)-1)]
res = sum(salary2)/len(salary2)
print(salary2)
print(res)