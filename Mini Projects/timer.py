# import time
# def countdown(t):
#     while t:
#         mins, sec = divmod(t, 60)
#         timer = '{:02d}:{:02}'.format(mins,sec)
#         print(timer,end='\r')
#         time.sleep(1)
#         t -=  1
#     print("Times Up!")
# t = int(input("Enter seconds for countdown : "))
# countdown(t)
import time
def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,sec)
        print(timer,end='\r')
        time.sleep(1)
        t -= 1
    print('Times Up!')
t = int(input("Start the timer for seconds : "))
countdown(t)