from func import is_unique
list_a = []

while len(list_a) != 7:
    a = int(input('Введите число: '))
    if a in list_a:
        print('Это число уже есть в списке')
    else:
        list_a.append(a)
print(list_a)
print(is_unique(list_a, 1))


# <---> [1, 2, 3, 4, 5]
for i in range(len(list_a)):
    for j in range(len(list_a)):
        if i == j:
            print(list_a[i], list_a[j])
        if i < j:
            print(list_a[i], list_a[j])

