from math import e, pi, sqrt

def normal_pdf(x=0, mu=0, sigma=1):
    return (1 / (sigma * sqrt(2 * pi))) * (e**(-(1/2))) * (((x - mu) / sigma)**2)


def normal_cdf(x=0, mu=0, sigma=1):
    vals = [num*0.001 for num in range(-1000, int(x*1000))]

    for val in vals:
        print(val)


print(normal_cdf())