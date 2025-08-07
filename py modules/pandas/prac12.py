import pandas as pd

dict = {'Keys': ['k1', 'k2', 'k1', 'k2'],
        'Name': ['Rahul', 'John', 'Randy', 'broke'],
        'House': ['Green', 'Red', 'Voilet', 'Red'],
        'Grade': ['8th', '9th', '10th', '11th']}

df = pd.DataFrame(dict)

print(df.pivot(index='Keys', columns='Name', values=['House', 'Grade']))