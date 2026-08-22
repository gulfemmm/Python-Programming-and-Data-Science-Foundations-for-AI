import numpy as np

#generate random
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter values > 25 and replace with 0
dataset[ dataset>25] = 0
print("Modified Dataset: \n", dataset)


# calculate summary stats
print("sum:",np.sum(dataset))
print("Mean:",np.mean(dataset))
print("standart Deviation:",np.std(dataset))