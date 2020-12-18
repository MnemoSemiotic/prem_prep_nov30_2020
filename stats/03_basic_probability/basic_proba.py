from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips.
  define one parameter, n, which represents the number of coin flips
  return a length n list of the random coin flips
'''