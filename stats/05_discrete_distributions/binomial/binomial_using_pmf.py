def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= 1
    return int(perm / factorial(k))


'''
PMF: Probability Mass Function
- Giving us the probability of a certain specific outcome
- can answer the binomial questions
- 3 params: 
    n : number of trials
    k : represents the number of successes
    p : is the probability of success of single trial (held constant)

'''

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

'''
What is the probability in 12 coin flips of a fair coin, that you get 7 heads?
'''
n = 12
k = 7
p = 0.5

print(binomial_pmf(n, k, p))