from random import randint

list_a = [randint(1, 100) for x in range(15)]
len_a = len(list_a)


def get_lists(list_a):
    list_first = []
    list_second = []
    for i in range(len(list_a)):
        if i < len_a / 2:
            list_first.append(list_a[i])
        else:
            list_second.append(list_a[i])
    return  list_second + list_first


print(list_a)
print(get_lists(list_a))
