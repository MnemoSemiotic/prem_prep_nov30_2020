from math import e

# print(e) # 2.718281828459045

def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num
    return prod

def poisson_pmf(lmbda, k):
    '''
    lmbda represents the average number of successes in a given volume of time or space, etc
    k is the number of successes for which you're trying to find the probability
    '''
    return lmbda**k * e**(-lmbda) / factorial(k)

# print(poisson_pmf(lmbda=10, k=10))

'''
You have a satellite that takes stellar images of random places in space. 
On average, each image has 30 stars in it. 
What is the probability that a given image has 25 stars in it?
'''

lmbda = 30
k = 25

# print(poisson_pmf(lmbda, k)) # 0.0511


'''
e is a constant, a factor of entropy, and it applies in a Poisson process

Criteria or Constraints for Poisson
- an average for a given volume/area/length of time
- each event needs to be independent
- assumption that the rate is consistent (iid. independent and identical distribution)
'''