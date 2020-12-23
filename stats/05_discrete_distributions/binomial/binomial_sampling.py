'''
Generalized Analytic Approach
1. Observe/Synthesize some phenomenon in nature
    - ex. sitting on a park bench and looking at the feet of
          geese, and marking 1 if they have black feet or 0
          if they have orange feet.
    - ex. counting in binary and summing the bits (for a fixed length of bits)

2. Create a means to organize and observe our results
    - ex. **packing values into a dictionary and printing them to terminal

3. Describe or interpret the phenomenon through the lens of our observations

'''

from random import choice, random

'''
using choice we are limited to a fixed value of p
'''

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

print(generate_n_bits(n=16))