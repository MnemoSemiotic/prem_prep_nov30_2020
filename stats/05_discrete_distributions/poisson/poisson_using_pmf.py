'''
You have a satellite that takes stellar images of random places in space. 
On average, each image has 30 stars in it. 
What is the probability that a given image has 25 stars in it?

'''

from math import e

# print(e) # 2.718281828459045

def factorial():
    pass

def poisson_pmf(lmbda, k):
    '''
    lmbda represents the average number of successes in a given volume of time or space, etc
    k is the number of successes for which you're trying to find the probability
    '''