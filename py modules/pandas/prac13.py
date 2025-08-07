import pandas as pd

dict = {'Name': ['Rahul', 'John', 'Randy', 'broke'],
        'House': ['Green', 'Red', 'Voilet', 'Red'],
        'Grade': ['8th', '9th', '10th', '11th']}

df = pd.DataFrame(dict)

print(df.melt(id_vars='Name', value_vars=['House', 'Grade'], var_name='House&Grades', value_name='Values'))
                                        # OR
# print(pd.melt(df, id_vars='Name', value_vars=['House', 'Grade'], var_name='House&Grades', value_name='Values'))