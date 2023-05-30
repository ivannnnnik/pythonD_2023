def get_list(list_a):
    a = list_a[2]
    b = list_a[len(list_a) - 2]
    list_a[2] = b
    list_a[len(list_a) - 2] = a
    return list_a


def is_unique(list_a, a):
    count_a = 0
    for i in list_a:
        if i == a:
            count_a += 1

    if count_a > 1:
        return False
    return True
