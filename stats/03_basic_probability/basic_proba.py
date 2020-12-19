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





