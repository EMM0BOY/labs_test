m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]


def round_to_two(x):
    return round(x, 2)


rounded_list = list(map(round_to_two, m))
print(rounded_list)
