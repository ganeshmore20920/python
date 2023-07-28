import random
passlen = int(input("Enter how long you wanna password : "))
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-"
p = "".join(random.sample(s,passlen))
print(p)