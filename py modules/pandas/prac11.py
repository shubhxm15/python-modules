import pandas as pd

data1 = {'Id': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06'],
         'Name': ['Tapu', 'Gogi', 'Goli', 'Pinku', 'Sonu', 'Champaklal']}

data2 = {'Id': ['E01', 'E02', 'E03', 'E04', 'E05', 'E013'],       # will show nan value in salary
         'Salary': [40000,50000,60000,70000,80000,90000]}

a = pd.DataFrame(data1)
b = pd.DataFrame(data2)

c = pd.merge(a,b, on = 'Id', how = 'left')
print(c)

data3 = {'Id': ['E07', 'E08', 'E09', 'E10', 'E11', 'E12'],
         'Name': ['Kshitij', 'Krish', 'Aayush', 'Japjot', 'Chetanya', 'Shubham'],
         'Salary': [2000,3000,5000,10000,50000,90000]}

data4 = {'Id': ['E07', 'E08', 'E09', 'E10', 'E11', 'E12'],
         'Name': ['Akshaansh', 'Maanit', 'Yaksh', 'Dev', 'Ram', 'Shyam'],
         'Salary': [20000,30000,40000,50000,60000,70000]}

d = pd.DataFrame(data3) 
e = pd.DataFrame(data4)

# f = pd.merge(data3, data4, on = 'Id')

print(pd.concat([d,e]))
