
# #num = [[a] for a in range(1,5)]

# #n = int(input())
# #num = list(a for a in range(1,n+1))
# #num2 = list(map(lambda x:x**2 , num))
# #num3 = list(map(lambda x:x**3,num))
# #for i in range(n):
# #    print(num[i]," : ",num2[i]," : ",num3[i])

# thickness = 50
# # c = 'H'
# # for i in range(thickness):
#     # print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
# # for i in range(thickness):
# #     print(c*i)
# # for i in range(thickness):
# #     print((c*i).rjust(thickness-1)+c+(c*i))
# print('hello world'.center(thickness
# stri = "ganeshonkarmore"
# print(stri[0:10])
# a = input().strip().split(" ")[1:]
# print(a)
# b = a.strip()
# a,b = input().split()
# print(a)
# print(b)

# x = "123654"
# print('2' in x)

# x = []
# for i in range(2):
#     x.append(input().split(" "))
# print(x)
# out = []
# for i in range(5):
#     out.append(0)
# print(out)

a = [5,6,9,2,1,4]
b = {5:"a" , 6:"b" , 9: "c" ,2:"d" ,1:"e" , 4: "f" }
for i in range(len(a)):
    print(b[a[i]])