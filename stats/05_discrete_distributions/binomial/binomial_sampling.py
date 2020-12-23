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

# print(generate_n_bits(n=16))


'''
Write a function called binary_sampling_dict that has two params
    num_bits
    num_samples

return a dict where the keys represent the number of successes,
and the values associated with those keys represent the count
of that number of successes occurring.

{
    0: 35,
    1: 63,
    ...
    num_bits: count of num_bits successes
}
'''
# 00101101 : 4 successes

def binary_sampling_dict(num_bits, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1

    return d

''' one trial of 100 samples '''
d = binary_sampling_dict(num_bits=16, num_samples=1000)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')