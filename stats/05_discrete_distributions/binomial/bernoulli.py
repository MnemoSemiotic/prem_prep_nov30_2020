'''
A random variable represents the outcome of an experiment.

Let Y = the result of processing 3 dice rolls of a 4-sided die
through this equation

Y = sum from i=1 to i=3 of: (1/4)**i * roll[i]
'''
from random import choice, random

def get_three_rolls():
    rolls = []
    for _ in range(3):
        rolls.append(choice([1,2,3,4]))
    return rolls

def outcome_of_Y():
    res = 0.0

    rolls = get_three_rolls()

    for idx, roll in enumerate(rolls, 1):
        res += (1/4)**idx * roll

    return res

# print(outcome_of_Y())

def dict_of_Y(num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        outcome = outcome_of_Y()
        if outcome not in d:
            d[outcome] = 0
        d[outcome] += 1

    return d

# for k, v in sorted(dict_of_Y(num_samples=100000).items()):
#     print(f'{k}: {v}')




'''
Bernoulli trial
single event with a binary outcome, with a set probability

If you have a bag full of red and blue balls, where you have
30 red balls, and 70 blue. If you reach into the bag thousands
of times and average the counts of these balls, what percentage 
would you expect of your draws would be red?

30%
'''

def bernoulli(p_success=0.5):
    draw = random() # gets a val betw 0 and 1

    if draw < prob_success:
        return True
    else:
        return False

print(random())