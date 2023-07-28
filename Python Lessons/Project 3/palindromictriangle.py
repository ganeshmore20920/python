a = int(input())
for i in range(1,a+1):
    print(((10**i-1)//9)**2)
n = input("Enter the word and see if it is palindrome: ") #check palindrome
if n == n[::-1]:
    print("This word is palindrome")
