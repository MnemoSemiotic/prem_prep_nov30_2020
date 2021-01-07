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


