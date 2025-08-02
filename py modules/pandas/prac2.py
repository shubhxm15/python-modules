import pandas as pd
from datasets import load_dataset       

dataset = load_dataset("lukebarousse/data_jobs")   # importing dataset from hugging face

load = dataset["train"].to_pandas()

# data = pd.read_excel("")
# data1 = pd.read_csv("")
# data2 = pd.read_json("")

print(load.head(5))    # provides top 5 values
print(load.tail(5))    # provides bottom 5 values

print(load.info(5))