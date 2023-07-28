import numpy as np
import pandas as pd
# construct dataframe from dictionaries of lists
data = {'Product Name' : ['Product A','Product B','Product C','Product D'],\
    'Product Price' :[2022,5021,3652,2522],\
        'Product Code' : ['A0' , 'B2', 'C25' , 'D25'],\
            'Product Category' : ['abc','pqr','xyz', 'def'],\
                'Selling Price' : [3000,6000,4000,3000]}
df = pd.DataFrame(data)
print("construct dataframe from dictionaries of lists")
print(df) 
print()

# construct dataframe from dictionaries of lists + specify the index 
# first way
data2 = {'ProductName': ['Product A', 'Product B','Product C'], 'ProductPrice' : [2250,2566,2366]}
df2 = pd.DataFrame(data2, index=['A','B','C'])
print("construct dataframe from dictionaries of lists + specify the index")
print(df2)
print()
# Second Way
product_IDs = ['A','B','C']
df22 = pd.DataFrame(data2, index=product_IDs)
print(df22)
print()

# Construct a Dataframe a list of dictionaries
data3 = [{'ProductName' : 'Product A', 'ProductPrice' : 2522},{'ProductName' : 'Product B', 'ProductPrice' : 4000},{'ProductName' : 'Product C', 'ProductPrice' : 3566}]
df3 = pd.DataFrame(data3)
print("Constructed a Dataframe a list of dictionaries")
print(df3)
print()

# Construct a dataframe from dictionary pandas series 
ser_name = pd.Series(['Product A','Product B','Product C'])
ser_price = pd.Series([2533,2566,6585])
data4 = {'Product Names' : ser_name , 'Product Prices' : ser_price}
df4 = pd.DataFrame(data4)
print("Constructed a dataframe from dictionary pandas series")
print(df4)
print()

# Construct a dataframe from list of list
data5 = [['Product A', 2568, 'ABC company'],['Product B',5698, 'XYZ company'],['Product C',4586,'PQR company']]
df5 = pd.DataFrame(data5)
df5.columns = ['Product name','Product Price','Company']
df5.index = ['A','B','C']
print("Constructed a dataframe from list of list")
print(df5)
print()

# Construct a dataframe in professional way
df6 = pd.DataFrame(data=[['Product A', 2568, 'ABC company'],['Product B',5698, 'XYZ company'],['Product C',4586,'PQR company']],\
    columns = ['Product name','Product Price','Company'] , index = ['A','B','C'])
print("professional way is ")
print(df6)