import pandas as pd
from datasets import load_dataset       

dataset = load_dataset("lukebarousse/data_jobs")    

load = dataset["train"].to_pandas()

df = load.iloc[109:115, 0:13]  # getting more data using iloc and slicing for a specific row and column

print(df)

dfs = load.job_title_short.unique()   # provides all roles under jobs title only once

print(dfs)