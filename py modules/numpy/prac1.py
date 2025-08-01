import random
import numpy as np
import statistics

basicsalary = [random.randint(50000, 100000) for _ in range(1000000)]

statistics.mean(basicsalary) # time taken is more than numpy

print(np.mean(basicsalary)) # time taken to compute by numpy is much lesser that statistics