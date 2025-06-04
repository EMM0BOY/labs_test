rounded_list = [3.47, 5.32, 4.01, 6.58, 15.01]


def is_greater_than_five(x):
    return x > 5


filtered_list = list(filter(is_greater_than_five, rounded_list))
print(filtered_list)
