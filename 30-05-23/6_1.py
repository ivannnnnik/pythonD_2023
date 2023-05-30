from func import get_list

list_a = []

flag = True
while flag:
    a = int(input('Введите число: '))
    if len(list_a) == 0:
        list_a.append(a)
    else:
        b = list_a[-1]
        if a % b != 0:
            break
        else:
            list_a.append(a)

print(list_a)
print(get_list(list_a))
