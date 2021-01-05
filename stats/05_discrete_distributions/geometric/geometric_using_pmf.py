'''
Geometric
- models the number of failures up until the first success
    - k means one of two things
        - the number of bernoulli trial failures before the first success
          or
        - the number of bernoulli trials up to and including the first success
'''


'''
Write the geometric_pmf function
3 parameters
p : probability
k : number of failures (inclusive or exclusive of the 1st success)
inclusive=True : whether or not to use inclusive or exclusive pmf
'''
def geometric_pmf(p, k, inclusive=True):
    if inclusive:
        return p * (1-p)**(k-1)
    else:
        return p * (1-p)**k



'''
You are handing out coupons for a restaurant. The probability that someone
accepts a coupon is 0.47. 
What is the probability that the first person who accepts a flier
is the third person you offer a flier?

'''
p = 0.47
k = 3

# print(geometric_pmf(p, k, inclusive=True))
# print(geometric_pmf(p, k-1, inclusive=False))


'''
You are flipping a fair coin. What is the probability that
you get your first heads on the 7th flip?
'''
p = 0.5
k = 7

# print(geometric_pmf(p, k, inclusive=True))
# print(geometric_pmf(p, k-1, inclusive=False))


'''
You have a series of routers transmitting packets of data.
There is a 0.99 probability that a given packet of data
passes through the router.
What is the probability that a given packet of data is 
lost in the 15th router?
'''
p = 0.01
k_inclusive = 15
k_exclusive = 14

# print(geometric_pmf(p, k_inclusive, inclusive=True))
# print(geometric_pmf(p, k_exclusive, inclusive=False))





'''
You have a series of routers transmitting packets of data.
There is a 0.99 probability that a given packet of data
passes through the router.
What is the probability that a given packet of data will pass
successfully through 14 routers?
0.99**14

What is the probability that a given packet will be dropped before
or on the 15th router it passes through?
'''

def geom_cdf_accum(p, k, inclusive=True):
    pass