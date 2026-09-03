import numpy as np

#Random variable: dice roll
outcomes =np.array([1,2,3,4,5,6])
probalities = np.array([1/6]* 6)

#Expectation
expectation = np.sum(outcomes * probalities)
print("Expectation (Mean): ",expectation)

#Variance and standart deviation
variance = np.sum((outcomes-expectation)**2*probalities)
std_dev = np.sqrt(variance)
print("Variance: ",variance)
print("Standard Deviation: ",std_dev)

