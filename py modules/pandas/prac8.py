import pandas as pd
from datasets import load_dataset
import numpy as np    

dataset = load_dataset("lukebarousse/data_jobs")    

data = dataset["train"].to_pandas()

data['Exact Location'] = data['job_location'] + ', ' + data['job_country']
# data['Exact Location'] = data['job_location'].str.capitalize + ', ' + data['job_country'].str.upper   
# capitalize for capitalizing the first word and upper will capitalize full word
print(data)