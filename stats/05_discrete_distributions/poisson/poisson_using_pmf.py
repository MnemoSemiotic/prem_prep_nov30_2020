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