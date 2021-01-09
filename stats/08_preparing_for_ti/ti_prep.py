''' TI Style Questions (2029-01-21) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs and Probability
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
        * Bayes Theorem

    * Understanding counting or binary through the lens of independent trials
        * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
        * trinary ex: [0, 1, 1, 2, 0]

    * Coding mathematical formulations

    * Analysis through Dictionaries
        * Pack values into dictionaries
            * Check membership vs not checking membership
        * Transform Dictionary values
        * General analytic approach
            * Create generative process
            * Load results into a dict
            * Interpret/Transform
'''


'''
Binomial
'''
def factorial(n):
    prod = 1
    for  num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return factorial(n) / (factorial(n-k)*factorial(k))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))


'''
Binomial Textbook Probs
You are sitting on a park bench watching city buses go by. On average,
two out of every 13 buses that goes by has an advertisement for
oat milk on it. What is the probability that, in one particular
set of observations, 10 out of 20 buses have oat milk ads on them?
'''
p = 2/13
k = 10
n = 20
# print(binomial_pmf(n,k,p))

''' what is the probability that less than 9 buses have oat milk adds?'''
# accum = 0.0
# for k_ in range(0, 8+1):
#     accum += binomial_pmf(n, k_, p)

# print(accum)


'''
Poisson
'''
from math import e

def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)

'''
Five stray cats walk on your chicken coop every 2 hours at night. 
What is the probability that 9 stray cats walk on the coop in
3 hours on a given night?

Constraints: time of night, seasonality, weather, other cats, don't affect the rate
'''
lmbda = 5 * (3/2) # 7.5
k = 9

# print(poisson_pmf(lmbda, k))


'''
Defining Random Vars and Coding Exploration of RVs
'''

'''
Define a process:
    Generate random lists of length n in base 4 {0,1,2,3}
    If a given value is drawn, then that value cannot be
    drawn on the next draw. No two values can be the same
    in a row.

Define an RV:
    The RV X represents a list of values generated in
    the process above put through this mathematical
    formulation.

    The first value will get multiplied by 1/4, the second value
    by 1/5, the third value by 1/6, and so on... and all of these
    will get summed together. 
'''
from random import choice

def get_dependent_quaternary(n=8):
    base_4 = [0,1,2,3]
    prior_val = -1

    quaternary = []

    for _ in range(n):
        if prior_val in base_4:
            choose_from = base_4.copy()
            choose_from.remove(prior_val)
        else:
            choose_from = base_4

        prior_val = choice(choose_from)
        quaternary.append(prior_val)

    return quaternary

# print(get_dependent_quaternary(n=8))


def get_rand_process_list(n=8):
    quart_list = get_dependent_quaternary(n)
    accum = 0.0

    for idx, val in enumerate(quart_list, 0):
        accum += val * 1/(4+idx)

    return accum, quart_list


def process_list(quart_list):
    accum = 0.0

    for idx, val in enumerate(quart_list, 0):
        accum += val * 1/(4+idx)

    return accum, quart_list


# print(process_list(n=8))

# -------------------------
outcomes_X = []

for num1 in [0,1,2,3]:
    for num2 in [0,1,2,3]:
        if num2 == num1:
            continue
        for num3 in [0,1,2,3]:
            if num3 == num2:
                continue
            for num4 in [0,1,2,3]:
                if num4 == num3:
                    continue
                for num5 in [0,1,2,3]:
                    if num5 == num4:
                        continue
                    for num6 in [0,1,2,3]:
                        if num6 == num5:
                            continue
                        for num7 in [0,1,2,3]:
                            if num7 == num6:
                                continue
                            for num8 in [0,1,2,3]:
                                if num8 == num7:
                                    continue
                                outcomes_X.append(process_list([num1,num2,num3,num4,num5,num6,num7,num8,]))

# for outcome in outcomes_X:
#     print(outcome)

print(min(outcomes_X))
print(max(outcomes_X))