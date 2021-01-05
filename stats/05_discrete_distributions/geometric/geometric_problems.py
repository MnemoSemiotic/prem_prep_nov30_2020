from geometric_using_pmf import *


'''
Geometric Breakout 1
Suppose you have an unfair coin, with a 68% chance of getting tails. 
What is the probability that the first head will be on the 3rd trial?
'''
p = 0.32
k = 3
print(geometric_pmf(p, k, inclusive=True))




'''
Differentiating Binomial, Poisson, Geometric, and basic probability
'''

# Binomial
# What is the probability that some number out of some number of events is successful?

# p=0.3, n=20, What is the probability that 18 (k) are successes? binomial_pmf(n, p, k)


# Geometric
# The proba of some binary event is p. What is the probability of having your
# first success on the kth trial?