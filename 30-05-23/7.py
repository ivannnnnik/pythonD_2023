list_a = []

len_list = int(input('Введите длину списка: '))

count_zero = 0
counter = 0

while counter != len_list:
    a = int(input('Введите число: '))

    if (counter == len_list - 2 and count_zero == 0 and a != 0) or (counter == len_list - 1 and count_zero == 1 and a != 0):
        print('Кол-во доступных элементов заканчивается \nВ списке должно быть минимум 2 элемента = 0')
    else:
        if a == 0:
            count_zero += 1
        list_a.append(a)
        counter += 1



def get_list(list_a):
    for i in range(2, len(list_a)):
        if list_a[i] == 0:
            list_a[i] = list_a[i - 1] + list_a[i - 2]
    return list_a

print(list_a)
print(get_list(list_a))