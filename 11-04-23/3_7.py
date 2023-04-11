from pprint import pprint

dict_students = {
    # 'Ф И О': 'Коэф. * ср. балл'
}


def get_st_rating():
    with open('students.txt', 'r+', encoding='utf-8') as our_file:
        for line in our_file:
            data = line.strip().split()
            key = f'{data[0]} {data[1]} {data[2]}'
            # key = data[0] + ' ' + data[1]+ ' ' + data[2]
            k = 0
            s = float(data[4])
            if s == 0:
                k = 1
            elif 0 < s < 2:
                k = 13
            else:
                k = 16
            dict_students[key] = float(data[3]) * k
        pprint(dict_students)


get_st_rating()
