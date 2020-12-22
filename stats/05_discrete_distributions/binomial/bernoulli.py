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

print(outcome_of_Y())
