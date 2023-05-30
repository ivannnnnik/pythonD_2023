from random import randint

count_num = int(input('Введите кол-во чисел в списке: '))
list_a = []
for i in range(count_num):
    list_a.append(randint(1, 100))

print(list_a)


def get_list(list_a):
    list_first = []
    list_second = []
    list_thrith = []
    for i in range(len(list_a)):
        if list_a[i] % 3 == 0:
            list_first.append(list_a[i])
            if list_a[i] % 5 == 0:
                list_thrith.append(list_a[i])
        elif list_a[i] % 5 == 0:
            list_second.append(list_a[i])
    return list_first, list_second, list_thrith


print(get_list(list_a))
