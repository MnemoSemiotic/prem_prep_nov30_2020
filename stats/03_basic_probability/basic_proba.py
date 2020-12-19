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

A = {HHHT, HHTH, HTHH, THHH} == three_heads
S == outcomes
'''
three_heads = []

for outcome in outcomes:
    if outcome.count('H') == 3:
        three_heads.append(outcome)

# print(len(three_heads))
# print(len(outcomes))
# print(len(three_heads) / len(outcomes))


'''
Suppose you call the function series_of_flips(14).
What is the probability that you get all 'H' values?

HHHHHHHHHHHHHH <----------
HHHHHHHHHHHHHT
HHHHHHHHHHHHTH
HHHHHHHHHHHHTT
...

first consider the probability P(H) for one flip:
0.5

H <----
T

next consider the P(HH) for two flips:
0.25

HH <---- A
HT
TH
TT

... P(HHH) ...
0.125 = 0.5 * 0.5 * 0.5 = 0.5**3

HHH <----
HHT
HTH
HTT
THH
THT
TTH
TTT

P(H 14 times) = 0.5**14 

'''


'''
Suppose you call the function series_of_flips(14)
What is the probability that you get at least one 'T' value?

HHHHHHHHHHHHHH <----------
HHHHHHHHHHHHHT
HHHHHHHHHHHHTH
HHHHHHHHHHHHTT
...

1 - 1/2**14 == (2**14 - 1) / 2**14



HHHH <---- 1/16
HHHT
HHTH
HHTT
HTHH
HTHT
HTTH
HTTT
THHH
THHT
THTH
THTT
TTHH
TTHT
TTTH
TTTT

1 - 1/16 = 15/16
'''


'''
How do we code a simulation that can, without mathematical formula
answer a question like "What is the probability of getting 3 heads 
in a row in 14 flips of a fair coin.
The 3 heads can occur in any way in a row.
'''

# num_samples = 100000 # 
# three_heads_in_a_row = []


# for _ in range(num_samples):
#     samp = series_of_flips(14)
#     if 'HHH' in ''.join(samp):
#         three_heads_in_a_row.append(samp)

# print(len(three_heads_in_a_row) / num_samples) # 0.637, 0.659, 0.651


'''
What is the probability of getting this exact series in 6 coin flips:
HTTHTH?

0.5**6

Note: A very different questions would be
What is the probability of getting exactly 3 tails in 6 coin flips?
could use nested for loops, or binomial_pmf
'''

'''
In three 6-sided dice rolls, what is the P of getting a sum of the 
three rolls below 6?

3 rolls    sum   outcome
5 4 2   =   11     F
1 2 1   =   4      T
'''

outcomes_S = []

for r1 in range(1, 6+1):
    for r2 in range(1, 6+1):
        for r3 in range(1, 6+1):
            outcomes_S.append([r1, r2, r3])

A = []

for roll in outcomes_S:
    if sum(roll) < 6:
        A.append(roll)

# print(len(A) / len(outcomes_S)) # ~0.0462



'''
In a probabilistic process, you roll 1 6-sided die, 
flip a coin, then roll a 12-sided die.

What is the probability that you'll get this exact sequence?
2, Heads, 7?

1/6 * 1/2 * 1/12

What is the probability that you'll get:
< 3, Tails, > 6 ?

2/6 * 1/2 * 6/12
'''


'''
you've got 100 of each toy in a giant bag, evenly mixed, 
what is the probability that you reach into the bag 5 times
and pull out one of each of these items (in any order)
pog, fidget spinner, tamagotchi (the other two can be anything)?

five_toys = ['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']
'''

five_toys = ['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']

all_toys_possible = []

for toy1 in five_toys:
    for toy2 in five_toys:
        for toy3 in five_toys:
            for toy4 in five_toys:
                for toy5 in five_toys:
                    all_toys_possible.append([toy1, toy2, toy3, toy4, toy5])

A = []

for toys in all_toys_possible:
    if 'pog' in toys and 'fidget spinner' in toys and 'tamagotchi' in toys:
        A.append(toys)

# for toys in all_toys_possible:
#     print(toys)

# print(len(all_toys_possible), 5**5) # how to think about cardinality

for toys in A:
    print(toys)
