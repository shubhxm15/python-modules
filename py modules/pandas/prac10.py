import pandas as pd
from datasets import load_dataset
import numpy as np    

dataset = load_dataset("lukebarousse/data_jobs")    

data = dataset["train"].to_pandas()
                                      # groupby is basically used to split df into groups based on unique values
# data = data.groupby('job_title_short').agg({'job_work_from_home': 'count'})    # we can also give double or triple parametes

data = data.groupby('job_title_short').agg({'salary_year_avg': 'max'})

print(data)
