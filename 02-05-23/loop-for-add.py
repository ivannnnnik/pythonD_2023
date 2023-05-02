list_a = [1, 2, 3, 4, 5, 6, 7]
# Удаление элемента по индексу

k = 0
for i in range(0, len(list_a)):
    if list_a[i] == 4:
        k = i

del list_a[k]

print(list_a)
