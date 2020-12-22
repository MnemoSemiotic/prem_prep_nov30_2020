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



