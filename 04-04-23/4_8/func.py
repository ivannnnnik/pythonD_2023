def get_pr(a, b):
    count_a = 1
    for i in a:
        count_a = count_a * i

    count_b = 1
    for i in b:
        count_b = count_b * i

    return count_a, count_b


def max_value(a, b):
    if a > b:
        return 'a'
    else:
        return 'b'
