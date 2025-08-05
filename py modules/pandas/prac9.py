import pandas as pd

data = {'Months': ['January', 'February', 'March', 'April', 'May']}

df = pd.DataFrame(data)
print(df ,'\n')

def short(value):
    return value[0:3]

df['short_months'] = df['Months'].map(short)  # so basically it calls a fxn and that fxn takes values which are under months and then extract only first 2 letters of that month and paste it in short_months column
print(df)