list_a = [5, 2, 3, 76]


def simple_func(simple_list):
    temp_min = 1000000000000
    temp_max = -100000000000

    for i in range(0, len(simple_list)):
        if temp_min > simple_list[i]:
            temp_min = simple_list[i]

        if temp_max < simple_list[i]:
            temp_max = simple_list[i]
        print(temp_max)

    return temp_min, temp_max


print(simple_func(list_a))
