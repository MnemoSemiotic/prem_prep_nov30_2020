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
list2 = ['skiing', 'basketball', 'ping pong', 'snowboarding', 'lacrosse']
list3 = ['rugby', 'skiing', 'water polo', 'curling', 'baseball']

def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)
    return set_intersect

print(intersection(list1, list2))