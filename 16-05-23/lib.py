def sqrt_num(x):
    a = x ** 0.5
    return a


def deg_num(y, z):
    b = y ** z
    return b


# 11.107 в) на сколько максимальный элемент больше минимального;
def get_list_sp(list_num):
    # [1 , 4, 46, 2, -1]
    # [-1, -4, -4]
    # [4, 5, 1]

    max_num = -10000000000
    min_num = 10000000000
    for i in list_num:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return max_num - min_num


