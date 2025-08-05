import pandas as pd

data1 = {'Id': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06'],
         'Name': ['Tapu', 'Gogi', 'Goli', 'Pinku', 'Sonu', 'Champaklal']}

data2 = {'Id': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06'],
         'Salary': [40000,50000,60000,70000,80000,90000]}

a = pd.DataFrame(data1)
b = pd.DataFrame(data2)

c = pd.merge(a,b, on = 'Id')
print(c)

data3 = {'Id': ['E07', 'E08', 'E09', 'E10', 'E11', 'E12'],
         'Name': ['Kshitij', 'Krish', 'Aayush', 'Japjot', 'Chetanya', 'Shubham']}

data4 = {'Id': ['E07', 'E08', 'E09', 'E10', 'E11', 'E12'],
         'Salary': [20000,30000,40000,50000,60000,70000]}

d = pd.merge(data3, data4, on = 'Id')

print(pd.concat([c,d]))