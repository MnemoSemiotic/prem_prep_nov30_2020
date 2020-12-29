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