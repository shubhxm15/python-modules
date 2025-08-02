import pandas as pd
from datasets import load_dataset       

dataset = load_dataset("lukebarousse/data_jobs")    

load = dataset["train"].to_pandas()

print(load.isnull().sum())     # shows sum of total values in all columns

df = load[['job_location', 'job_title_short']].tail(5)  # to obtain specific data from dataset

print(df)