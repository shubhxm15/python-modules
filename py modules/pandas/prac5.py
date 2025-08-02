import pandas as pd
from datasets import load_dataset       

dataset = load_dataset("lukebarousse/data_jobs")    

load = dataset["train"].to_pandas()

print(load.describe())       # perform different functions on those columns with numerical value

df = [(load.job_title_short == 'Software Engineer') | (load.salary_year_avg.notna())]   # to compare different columns using or, and
# df = [(load.job_title_short == 'Data Analyst') | (load.salary_year_avg > 100000)]

print(df)