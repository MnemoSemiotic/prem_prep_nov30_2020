'''
How to count in Binary
consider
00
01
10
11

DEC  BIN
0: 0000
1: 0001
2: 0010
3: 0011
4: 0100
5: 0101
6: 0110
7: 0111
8: 1000
9: 1001
10:1010
11:1011
12:1100
13:1101
14:1110
15:1111


1      1       0      1
8's     4's   2's  1's place

1*8 + 1*4 + 0*2 + 1*1
8 + 4 + 0 + 1 = 13


Can think of a binary number (word) as being a series of 
successes and failures
1 1 0 0
S S F F

The count of 1's in a 4-bit binary will follow a binomial distribution

0: *
1: ****
2: ******
3: ****
4: *

0: 1/16
1: 4/16
2: 6/16
3: 4/16
4: 1/16
'''


'''
count in 4-bit binary
'''

def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')


'''
7 minutes!

Code the dec_to_bin function.
Should take as input 2 things:
    a decimal value (dec)
    a number of bits (n_bits=8)

algorithm
Given a decimal number
    - take the modulus by 2
        - set aside the result
    - floor divide the number by 2
        - until that number is 0
    - reverse the sequence of outcomes

dec_to_bin(43)

--------------
43 % 2     ==> 1
43 // 2 = 21
21 % 2     ==> 1
21 // 2 = 10
10 % 2     ==> 0
10 // 2 = 5
5 % 2      ==> 1
5 // 2  = 2
2 % 2      ==> 0
2 // 2  = 1
1 % 2      ==> 1
1 // 2  = 0
reversed ==> 101011 is the binary representation of 43
'''
def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1]# list(reversed(bin_list))

# print(dec_to_bin(43, 16))

# print(list(reversed([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1])))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d

# for dec, bin_ in get_binary(n_bits=16).items():
#     print(f'{dec}: {bin_}')























