# our_file = open('data.txt')
# our_file.close()


def get_max_val(file_name):
    file_max = -100000000
    with open(file_name, 'r+', encoding='utf-8') as our_file:
        for line in our_file:
            number = int(line.strip())

            if number > file_max:
                file_max = number

            # print(number)
    with open('max_val1.txt', 'w+', encoding='utf-8') as our_file:
        our_file.write(str(file_max))

    return file_max


print(get_max_val('data.txt'))
