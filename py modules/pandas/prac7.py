import pandas as pd
from datasets import load_dataset
import numpy as np    

dataset = load_dataset("lukebarousse/data_jobs")    

load = dataset["train"].to_pandas()
                                                                       # creating columns and filling values based on other values
                                                                       # creating new columns using existing columns
load.loc[(load['salary_year_avg'] > 100000), "In_short"] = "Enough"
load.loc[(load['salary_year_avg'] < 100000) | (load.salary_year_avg.isnull()), "In_short"] = "Not Enough"


print(load.iloc[20:30])