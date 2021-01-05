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

print(geometric_pmf(p, k, inclusive=True))
print(geometric_pmf(p, k-1, inclusive=False))