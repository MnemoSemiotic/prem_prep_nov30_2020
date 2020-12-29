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


3 general types
    - Counting Approach
    - Closed Formula Approach
    - Sampling Approach
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
d = binary_sampling_dict(num_bits=16, num_samples=100)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


# ''' one trial of 1000 samples '''
# d = binary_sampling_dict(num_bits=16, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' one trial of 10000 samples '''
# d = binary_sampling_dict(num_bits=16, num_samples=10000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' 500 trials of 1000 samples '''
def binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)

    return d_out

# d = binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


# for k, v in sorted(d.items()):
#     print(f'{k}: {v / sum(d.values())}') # averaged (observed) probability




'''-----------------'''
''' using random(), we can change our p value '''

def get_success(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

# print(get_success(0.25))

def generate_n_successes(n=8, p=0.5):
    lst = []
    for _ in range(n):
        lst.append(get_success(p))
    return lst

# print(generate_n_successes(n=8, p=0.05))

# verify, as 12*0.25 = 3
test_trials = 100000
trial_results = []
for _ in range(test_trials):
    trial_results.append(generate_n_successes(12, p=0.75).count(1))

print(sum(trial_results) / test_trials)