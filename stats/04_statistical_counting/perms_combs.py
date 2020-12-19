five_toys = ['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']

'''
You have 5 toys in a bag. You pull them out one at a time and 
you don't put them back in. In how many different orders
can you pull out these 5 toys?

5! = 120

['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']
['red truck', 'pog', 'fidget spinner', 'gi joe', 'tamagotchi']
['red truck', 'pog', 'gi joe', 'fidget spinner', 'tamagotchi']
...

'''

def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

print(factorial(0))