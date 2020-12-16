'''
Random Experiment
'''

from random import choice

'''
RE of a single coin flip
'''

def coin_flip():
    # return choice('HT') # equivalent alternative
    return choice(['H', 'T'])

# print(coin_flip())


'''
RE: the count of heads in 20 flips
'''
def twenty_flips():
    flips = []

    for _ in range(20):
        flips.append(coin_flip())

    return flips

# print(twenty_flips())


'''
How many heads would you "Expect" in 20 flips?
0.5 * 20 = 10
'''


'''
list/set trick
- remove duplicates through set properties
'''

lst = [8,7,9,7,6,4,3,5,1,3,2,4,6,8,6]
l1 = list(set(lst))

# print(l1)


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)

    return deduped

# print(dedupe_in_order(lst))


'''
Star (*) args
'''
def star_args(*args):
    print(type(args))
    for item in args:
        print(item)
    return None

# star_args('hi', 0.546, 'elephant', 5, True, None, [1,2,3,4,6])




'''
Union
'''
list1 = ['basketball', 'baseball', 'soccer', 'rolf ball', 'ping pong', 'backgammon']
list2 = ['skiing', 'basketball', 'ping pong', 'snowboarding', 'lacrosse']
list3 = ['rugby', 'skiing', 'water polo', 'curling', 'baseball']

def union(set1, set2):
    set_union = set1.copy()

    for item in set2:
        if item not in set_union:
            set_union.append(item)

    return set_union

# print(union(list1, list2))


def union_mult_sets(*mult_sets):
    set_union = []

    for lst in mult_sets:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    
    return set_union

# print(list1, list2, list3)

'''
Intersection
'''
list1 = ['basketball', 'baseball', 'soccer', 'rolf ball', 'ping pong', 'backgammon']
list2 = ['skiing', 'basketball', 'ping pong', 'snowboarding', 'lacrosse', 'baseball']
list3 = ['rugby', 'skiing', 'water polo', 'curling', 'baseball']

def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)
    return set_intersect

# print(intersection(list1, list2))

def intersection_mult(*args):
    set_intersect = []

    if len(args) > 1 and len(args[0]) > 0:
        for item in args[0]:
            is_member = True

            for set_ in args[1:]:
                if item not in set_:
                    is_member = False
                    break

            if is_member:
                set_intersect.append(item)

    return set_intersect

# print(intersection_mult(list1, list2, list3))


'''
Set Difference
A - B
'''
def difference(set1, set2):
    set_difference = []

    for item in set1:
        if item not in set2:
            set_difference.append(item)
    return set_difference


# print(difference(list1, list2))
# print(difference(list2, list1))


'''
Complement
'''
list1 = ['basketball', 'baseball', 'soccer', 'rolf ball', 'ping pong', 'backgammon']
list2 = ['skiing', 'basketball', 'ping pong', 'snowboarding', 'lacrosse', 'baseball']
list3 = ['rugby', 'skiing', 'water polo', 'curling', 'baseball']

extra_stuff = ['chess', 'rowing']

sample_space = union_mult_sets(list1, list2, list3, extra_stuff)

def complement(sample_space, set1):
    return difference(sample_space, set1)

# print(complement(sample_space, list1))


'''
Breakout Slide 8
'''

# Which of the following would not be considered a random experiment? Why?
# A. The selection of a numbered ball from a bucket of numbered balls (1-50)
# B. The amount of time needed to wait for a taxi cab
# C. Randomly selecting a colored marble from an urn full of numbered balls
# C sounds impossible


# Write out the sample space for the random experiment which is defined as sequentially completing the following steps:
# First, rolling a fair four-sided die
# Then, flipping a coin
# Last, flipping the coin again
# 	{1HH, 1HT, 1TH ...

four_sided = [1,2,3,4]
fair_coin1 = ['H', 'T']
fair_coin2 = ['H', 'T']

samp_space = []

for roll in four_sided:
    for flip1 in fair_coin1:
        for flip2 in fair_coin2:
            samp_space.append([roll, flip1, flip2])

# for outcome in samp_space:
#     print(outcome)

# List the sample points in the following events:
# A = The event in which the die roll results in exactly one pip showing
A = []
for outcome in samp_space:
    if outcome[0] == 1:
        A.append(outcome)

# for outcome in A:
#     print(outcome)

# B = The event in which at least one of the coin flips results in heads
B = []
for outcome in samp_space:
    if outcome.count('H') >= 1:
        B.append(outcome)

# for outcome in B:
#     print(outcome)

# List the sample points which are in the Union of events A and B from above
# print(union(A, B))

[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [1, 'T', 'T'], [2, 'H', 'H'], [2, 'H', 'T'], [2, 'T', 'H'], [3, 'H', 'H'], [3, 'H', 'T'], [3, 'T', 'H'], [4, 'H', 'H'], [4, 'H', 'T'], [4, 'T', 'H']]



# print(complement(samp_space, union(A, B)))
[[2, 'T', 'T'], [3, 'T', 'T'], [4, 'T', 'T']]


'''
Breakout Slide 17
'''

# Let our sample space be rolling two 6-sided dice.
sample_space = []

for roll1 in range(1, 6+1):
    for roll2 in range(1, 6+1):
        sample_space.append([roll1, roll2])

# for outcome in sample_space:
#     print(outcome)

# Event A: any roll with a sum greater than or equal to 10
# Event B: any roll with an even sum

A, B = [], []

for outcome in sample_space:
    if sum(outcome) >= 10:
        A.append(outcome)
    if sum(outcome) % 2 == 0:
        B.append(outcome)

# What do our events A and B look like?
# print('A:')
# for outcome in A:
#     print(outcome)

# print()

# print('B:')
# for outcome in B:
#     print(outcome)

# What is A - B?
# print(difference(A, B))

# print()
# # What is B - A?
# print(difference(B, A))