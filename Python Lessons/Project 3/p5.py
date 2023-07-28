# for i in range(6):
#     print("  ",end=('  '))
#     print('               '.center(25,'H'))
#print 'HackerRank'.ljust(width,'-')\
t = 5
c = "H"
for i in range(t):
    print((c*i).rjust(t-1)+c+(c*i).ljust(t-1))
for i in range((t+1)//2):
    print((t*c*5).center(t*6))