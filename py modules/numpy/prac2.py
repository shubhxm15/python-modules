import numpy as np

job_title = np.array(['engineer', 'ai engineer', 'data analyst', 'civil engineer', 'sde'])

salary = np.array([30000, 60000, 80000, 15000, np.nan])  # nan is a special float point value. The type of nan is float

bonus_rate = np.array([0.09, 0.15, .05, .2, np.nan])

total_salary = salary * (1 + bonus_rate)   # int + float (in case of np.nan)
print(total_salary)   

print(np.mean(total_salary))  # this method is not meant to handle nan values

print(np.nanmean(total_salary))