'''
A random variable represents the outcome of an experiment.

Let Y = the result of processing 3 dice rolls of a 4-sided die
through this equation

Y = sum from i=1 to i=3 of: (1/4)**i * roll[i]
'''
from random import choice

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

for k, v in sorted(dict_of_Y(num_samples=1000).items()):
    print(f'{k}: {v}')