# list_a = [9, 2, 4, 56]
# len_list = len(list_a)
#
# i = 0
# while i != len_list:
#     print(list_a[i])
#     i += 1
#
#


# while True:
#     a = int(input('Введите число: '))
#     print(a ** 2)
#

a = [1, 3, 4, 6, 7, 4, 3]

i = 0
while i != len(a):
    if a[i] == 6:
        print('Имеется')
        break
    else:
        i += 1


i = 1
while True:
    print(i)
    i += 1
    if i == 11:
        break
