import pandas as pd
from datasets import load_dataset
import numpy as np    

dataset = load_dataset("lukebarousse/data_jobs")    

load = dataset["train"].to_pandas()

print(load.isnull().sum())             # gives total sum of na values in each column

print()

# b = load.dropna()                   # it will remove all those columns with one or more na values
# c = load.replace(np.nan, 20)      # this will replace all the nan values with 20

d = load['job_title'] = load['job_title'].replace(np.nan , "Majdur")     # will only replace nan value under job_title
print(d)

print(load.fillna(method = 'bfill'))    # bilateral fill - fill na values with same as the lower value
print(load.fillna(method = 'ffill'))    # forward fill   - fill na values with same as the upper value