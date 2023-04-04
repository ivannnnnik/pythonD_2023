from func import get_pr, max_value

n = 10
m = 10

a = [1, 2, 5, 8]
b = [1, 2, 5, 7]

count_a, count_b = get_pr(a, b)  # Получаем значения перемноженных элементов списка a и списка b
result = max_value(count_a, count_b)  # Определяем максимальное значение перемноженных элементов списков

print(result)
