from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips.
  define one parameter, n, which represents the number of coin flips
  return a length n list of the random coin flips
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

print(series_of_flips(4))