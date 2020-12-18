from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips.
  define one parameter, n, which represents the number of coin flips
  return a list of length n containing n random coin flips
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(4))


'''
Write a function called four_flip_sample_space that takes 
no arguments. It should return a list of all 
possible outcomes for 4 coin flips.
[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H'],
    ['H', 'H', 'T', 'T'],
    ...
    ['T', 'T', 'T', 'T'],
]
'''

def four_flip_sample_space():
    flip = ['H', 'T']
    outcomes = []

    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    outcomes.append([f1,f2,f3,f4])
    return outcomes

outcomes = four_flip_sample_space()

# for outcome in outcomes:
#     print(outcome)


'''
What is the probability that in 4 coin flips, you get exactly 3 heads?
write code that traverses the outcomes and delivers P(3heads) = |3heads| / |outcomes|
'''
