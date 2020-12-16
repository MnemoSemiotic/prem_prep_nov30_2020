'''
Random Experiment
'''

from random import choice

def coin_flip():
    # return choice('HT') # equivalent alternative
    return choice(['H', 'T'])

# print(coin_flip())


# 20 flips
def twenty_flips():
    flips = []

    for _ in range(20):
        flips.append(coin_flip())

    return flips

print(twenty_flips())