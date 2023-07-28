from concurrent.futures import process
import numpy as np
import pandas as pd
products = [10,20,30,40,50]
print("List :", products, type(products))
# List to numpy array
array = np.array(products)
print("numpy array is : " , array , type(array))
# numpy array to pandas series
series = pd.Series(products)
print("Pandas series is :" , series , type(series))
# print(series.size)
# print(array.size)
series.name = "Product Prices" # Giving name to the series
print("Product Series name :",series.name)
# Types of Indexing
"""1.Zero Based or Position Based
   2.Label Based Indexing"""
print("Zero based indexing or position based indexing:", series.index) # RangeIndex(start=0, stop=5, step=1)
print("Label based or Axis based indexing :", series[2]) # 30
# print(type(series.index)) # <class 'pandas.core.indexes.range.RangeIndex'>
# print(list(series.index)) # [0, 1, 2, 3, 4]
product_categories = pd.Series({"Product A ": 10 , "Product B " : 20, "Product C " : 30})
#Dictionaries to Pandas series
print(product_categories) # Dictionary key value becames series index and values.
"""print(product_categories.index)""" #Index(['Product A ', 'Product B ', 'Product C '], dtype='object')
"""print(type(product_categories.index))"""  # <class 'pandas.core.indexes.base.Index'>