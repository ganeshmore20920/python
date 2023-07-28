# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime  
from datetime import date 
# date=str(input())
# month, day, year = date.split(' ')  
month, day, year = map(int,input().split())   
day_name = datetime.date(year,month,day) 
print(day_name.strftime("%A").upper()) 


# import datetime
# from datetime import date
# month,day,year = map(int,input().split())
# day_name = datetime.date(year,month,day)
# print(day_name.strftime("%A").upper())