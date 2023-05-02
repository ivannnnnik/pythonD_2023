list_a = [12, 4.6, 4.6, 'str', True, None]

c = 'adas'

# Добавление элемента
list_a.append(12)
list_a.append(c)

# Удаление по индексу
list_a.pop(0)
print(list_a)

# Сортировка
list_num = [4, 21, 8, 4]
list_str = ['ba', 's', 'bb', 'd']

list_num.sort()
list_str.sort()

print(list_num)
print(list_str)

# Полное очистка списка
# list_a.clear()
print(list_a)

# Удаление первого по вхождению элемента
list_a.remove(4.6)
print(list_a)

# кол-во элементов с определенным значением
count = list_a.count(12)
print(count)

# склеивание
list_a.extend(list_num)
print(list_a)
