from random import choice

def get_bit():
    return choice([0,1])


def get_binary(n=8):
    return [get_bit() for _ in range(n)]

    # return_list = []

    # for _ in range(n):
    #     return_list.append(get_bit())

    # return return_list

# print(get_binary(16))

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return bin_list


print(get_float(8))

