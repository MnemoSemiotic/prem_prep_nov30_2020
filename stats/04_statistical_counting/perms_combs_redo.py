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