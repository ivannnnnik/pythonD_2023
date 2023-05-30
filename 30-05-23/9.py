list_a = [1, 1, 4, 5, 6, 6, 7, 7, 3, 34, 43, 5, 6, 31, 31]


def get_list(list_a):
    count_pair = 0
    max_pair = 0
    for i in range(len(list_a) - 1):
        if list_a[i] == list_a[i + 1]:
            print("Пара:", list_a[i], list_a[i + 1], "Индексы: ", i, i + 1)
            count_pair += 1
            if list_a[i] > max_pair:
                max_pair = list_a[i]
    print("Кол-во пар", count_pair)
    print("Пара с макс значением: ", max_pair)


get_list(list_a)