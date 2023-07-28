# your code goes here
print("You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).")
print("Enter here 0 for $1.000.000 and 1 for $0.01")
a = int(input("Enter your choice : "))
b = 30
amount = 0.01 * (2**b)
if(a==1):   
    print(f'your money will be ${amount} \n you could get just $1,00,000 ')
elif(a==0):
    print(f"You will get $1.00,000 \n otherwise you could get {amount}")
else:
    print("Invalid Input ")
