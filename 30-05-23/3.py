list_a = [1, 2, 3]
list_b = [1, 2, 3, 4]

if len(list_a) != len(list_b):
    if len(list_a) > len(list_b):
        while len(list_b) != len(list_a):
            a = int(input('Введите число: '))
            list_b.append(a)
    else:
        while len(list_b) != len(list_a):
            a = int(input('Введите число: '))
            list_a.append(a)


def sq_list(list_a, list_b):
    list_c = []
    for i in range(len(list_a)):
        b = list_b[i] * list_a[i]
        list_c.append(b)
    return list_c

print(sq_list(list_a, list_b))