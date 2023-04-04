from random import randint
from pprint import pprint

# Ключ - сумма двух костей, значение - кол-во выпадений в %
dict_temp = {}

count = 1000


def get_sum():
    k_1 = randint(1, 6)
    k_2 = randint(1, 6)
    return k_1 + k_2


for i in range(count):
    random_sum = get_sum()  # Сумма двух костей

    if random_sum in dict_temp:
        dict_temp[random_sum] = dict_temp[random_sum] + 1
    else:
        dict_temp[random_sum] = 1
pprint(dict_temp)

for key in dict_temp:
    dict_temp[key] = dict_temp[key] / count * 100  # Подсчет кол-ва в %

pprint(dict_temp)
