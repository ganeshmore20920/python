import pandas as pd
# print(pd.__version__)
products = ["a","b","c","d"]
# type(products)
product_categories = pd.Series(products)
print(product_categories)