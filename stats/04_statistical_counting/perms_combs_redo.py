'''
Factorial
- provides cardinality nPk where n == k
'''
def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

# print(factorial(5))

'''
Permutations
nPk = n! / (n-k)!
if k==n =>
    5! / (5-5)!
    5! / 0!
    120 / 1
'''


'''
You have 10 students and you are conducting a science fair where 4 students will win
1st, 2nd, 3rd, 4th. How many different arrangements of those 4 winners is possible?
'''

def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

# print(permutations(5, 5))
# print(permutations(10, 4))
# print(10*9*8*7)

def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

# print(permutations(5, 5))
# print(permutations(10, 4))


'''
Permutations Intuition
- count normally
- reduce the space by eliminating duplicates

Five pets and 5 beds. What are all the ways that you can
arrange those 5 pets in 5 beds?
'''
base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

animal_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break
    if perm == True:
        animal_perms.append(an_number)

# for an_number in animal_perms:
#     print(an_number)


'''
Combinations
nCk = n! / ((n-k)! * k!)
'''
def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

''' How many 3 card combos from a 52 card deck?'''

# print(combinations(52, 3))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))
    
# print(combinations(52, 3))


'''
Combs Intuition

Out of a set of 11 basketball players, only
5 can be on the court at a time. What are all
the combinations possible for that basketball team.
'''
# print(combinations(11, 5))

'''
What are the combinations of teams that can be on the court?
'''

# an expensive counting approach
num_combs = combinations(11, 5)

def basketball_combs():
    eleven_nums = range(1, 11+1)

    # every arrangement of 5
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])

    # for five in possible_five:
    #     print(five)

    perms = []

    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

    # for five in perms:
    #     print(five)

    combs = []

    for five in perms:
        sorted_five = sorted(five)

        if sorted_five not in combs:
            combs.append(sorted_five)
    
    return combs

# for five in basketball_combs():
#     print(five)




# an expensive sampling approach

'''
We can sample 5 players from our list of 11,
can continue to build combinations until we reach
11C5 combinations
'''

from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combinations(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)

        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs


team_size = 21
num_players = 5

# print(len(basketball_combs_samp(team_size, num_players)))
print(combinations(team_size, num_players))
