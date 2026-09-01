#Problem
#-A disase affects 1% of a population
#- A test is 95% accurate for disased individuals 90% accurate for non-disased indiv
#-Find the probabilty of having the disase given a positive test result

def bayes_theorem(prior,sensivity,specificity):
    evidence =(sensivity*prior) + ((1-specificity) * (1-prior))
    posterior = (sensivity*prior)/ evidence
    return posterior

prior =0.01 #1% prevalance
sensivity = 0.95 #True positive rate
specificity = 0.90 #true negative rate

posterior = bayes_theorem(prior,sensivity,specificity)
print("Probablity of Disease Given Positive Test: ",posterior)