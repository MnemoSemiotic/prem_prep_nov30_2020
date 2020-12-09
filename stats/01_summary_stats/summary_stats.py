def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)


# data from the prior slide
a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(a)
# print(mean(a))
# print(mean(a, trim_by=1))
# print(mean(a, trim_by=2))


'''
Breakout Slide 10

An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.
Urban: 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
Farmhouse: 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3
'''
'''
A. Determine the sample mean for each group.
'''
urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# print(f'Sample Mean Urban: {round(mean(urban), 1)}')
# print(f'Sample Mean Farmhouse: {round(mean(farmhouse), 1)}')

'''
B. Determine the trimmed mean for each group by trimming the smallest and largest value from each group.
'''
# print(f'Sample Trimmed Mean Urban: {round(mean(urban, trim_by=1), 1)}')
# print(f'Sample Trimmed Mean Farmhouse: {round(mean(farmhouse, trim_by=1), 1)}')


'''
Median
'''

def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    else:
        upper_mid_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_mid_idx-1], lst_sorted[upper_mid_idx]])

odd = [13, 18, 13, 14, 13, 16, 35, 21, 13]
even = [15, 14, 10, 8, 12, 8, 16, 13]

# print(sorted(odd))
# print(median(odd))

# print(sorted(even))
# print(median(even))


'''
Breakout Slide 16

An article published in the journal, Indoor Air, considered two different air samples
 to test for endotoxin concentrations, the first in urban households, and the second 
 in farmhouses.
Urban: 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
Farmhouse: 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0

Calculate the Median of both groups

'''
urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]

# print(sorted(urban))
# print(f'Median Urban: {round(median(urban), 1)}')
# print(sorted(farmhouse))
# print(f'Median Farmhouse: {round(median(farmhouse), 1)}')



'''
f-strings
- dynamically interpolate values into strings

'''
some_float = 8.5
some_int = 10

some_str = f'The sum of {some_float} and {some_int} is {some_float + some_int}'

print(some_str)