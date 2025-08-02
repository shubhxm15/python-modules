import pandas as pd

data = {"Name": ['Rahul', 'Rohan', 'Rohit'],
        "Age": [20, 24, 23],
        "Salary": [40000, 45000, 50000]}

a = pd.DataFrame(data)          # Creating dataframes using list and tuples
print(a)