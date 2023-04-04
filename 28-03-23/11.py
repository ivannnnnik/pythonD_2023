# a = 10  # 1 day
# b = 10  # %

d = int(input('Введите день: '))


def simple(a, b, d):
    temp = a
    for i in range(2, d + 1):
        c = (temp * (100 + b)) / 100
        temp = c
    return temp


print(simple(10, 10, d))
