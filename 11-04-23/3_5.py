from random import randint

list_random_number = []


while len(list_random_number) != 6:
    number = randint(1, 49)
    if number not in list_random_number:
        list_random_number.append(number)

# Чтение файла / Контекстный менеджер


# r / r+  -- > чтение / чтение + создание файла, если его нет
# w / w+  -- > запись / запись + создание файла, если его нет
# rw  -- > чтение + запись файла
# data = 'Hello\nWorld'  --- > Перевод на следующую строку
# content = [int(content[i]) for i in range(len(content))]
# Построчное чтение файла
# with open('data.txt', 'r') as our_file:
#     for line in our_file:
#         print(line.strip())


list_our_number = []
with open('data.txt', 'r') as our_file:
    content = our_file.read()
    # strip - убирает лишние элементы табуляции
    # split - разделяет элементы по разделителю и добавляет их в список
    content = content.strip().split()
    for i in range(len(content)):
        content[i] = int(content[i])

    list_our_number = content

# sort - сортировка по возрастанию

list_our_number.sort()
list_random_number.sort()

print('Наш билет: ', list_our_number)
print('Выигрышный билет: ', list_random_number)
