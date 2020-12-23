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
        perm *= i
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

# print(binomial_pmf(n, k, p))


'''
Sitting on a park bench you observe geese walking by. There's a probability
of 0.3 that any goose walking by has black feet. What is the probability
that 4 out of the next 12 geese walking by has black feet?
'''
n = 12
k = 4
p = 0.3

# print(binomial_pmf(n, k, p))

'''
At the dog park, there is a 0.4% chance that any one dog you see is a german shepherd.  What is the probability that 6 out of the 14 dogs at the park are german shepherds?
'''
n = 14
k = 6
p = 0.4

# print(binomial_pmf(n, k, p))

'''
There is probability of .5 that there will be a snow storm. What is the probability that 3 out of the remaining 9 days of this year, there will have snow storm?
'''
n = 9
k = 3
p = 0.5
# print(binomial_pmf(n, k, p))

'''
One in three adults suffer from allergies during the months of April through June. What is the probability that 6 out of 30 adults will suffer from Allergies during the months of April through June?
'''
n = 30
k = 6
p = 1/3
# print(binomial_pmf(n, k, p))

'''
Probability of catching Salmon in a river is  0.02. What is the probability of catching 3 Salmons in the 300 caught fish?
'''


'''
Sitting on a zoom call, you are asked to write come code. The probability that you know what to do is 0.1. What is the probability that out of 10 coding challenges, you will be able to do 5 challenges?
'''


'''
Sam says "70% choose chicken, so 7 of the next 10 customers should choose chicken" ... what are the chances Sam is right?
'''



'''
You go out fishing. There's a probability of 0.2 that a fish is  a salmon. What is the prob that 4 out of the next 100 fishes are salmon?
'''

'''
I have 2 kinds of beers in my fridge (lots of them). There is a 0.5 chance to get the IPA. What is the probability to get an IPA 7 times out of 10 beers?
'''

'''
You are a biologist and have blonde hair. Your spouse has darker hair ans youunderstand the concept of dom and sub genes. There is a .25% probability that your child will have blonde hair. What is the probabilty that 3 of your 17 children will have blonde hair?
'''


'''There are 6 seats in a flight. 2 of them on windows seats, 2 are aisle, 2 are middle seats. What is the probability you will sit in the middle seat on your departure and return flight. 
p = 2/6
n = 2
k = 2


What is the probability that out of the next 8 flights, you are assigned the middle seat 5 times?
p = 2/6
n = 8
k = 5
'''


'''A restaurant offers 12 items its menu. The probability that menu item 2 is ordered is 0.2. What is the probability that out of 21 guest, guest number 5 orders menu item 2.
'''
p = 0.2
n = 1
k = 1



'''
from a sack of toys, theres a probability of 0.7 that the toy will be a ball. what is the probability that 5 out of 10 trials will be balls. (Assume the probability of choosing a ball will not change across trials)
'''


'''
At a circus you observe clowns tumbling by. There’s a probability of .4 that any clown walking by has a blue shirt. What is the probability that 4 of next 14 clowns has a blue shirt.
'''


'''
You are a librarian observing fiction and nonfiction circulation. There is a probability of .23 that any book checked out will be non-fiction. What is the probability that 20 out of the next 50 books to be checked out will be fiction?
'''


'''
Birding at Eagle Creek there's a 0.2 chance you'll see a Great Egret. In the next 15 birds you see what's the probability 7 will be Great Egrets.
'''


'''
You are rescuing a dog in a dog shelter.  There is a probability of .28 that you will see a poodle.  What is the probability that 9 dogs will be a poodle out of 50.
'''



'''
CDF
Cumulative Distribution Function
- cumulative implies accumulator
- cumulative probability between 0 and some value of k (inclusive)
'''

def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative

'''
You have 14 components in a circuit. At any given time,
there is a 95% chance that a given component is functioning.
What is the probability that 12 or more components are functioning
in a circuit that has 20 components?
'''
n = 20
k_high = 11
p = 0.95

print(1 - binomial_cdf(n, k_high, p))

# binomial_pmf(n, 12, p) + binomial_pmf(n, 13, p) + ... + binomial_pmf(n, 20, p)
