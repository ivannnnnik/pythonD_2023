class Car:
    """Описание класса"""
    count_r = 4  # Статический атрибут
    def __init__(self, color='Red', name):
        self.color = color
        self.name = name
    @staticmethod
    def start_engine():
        print('Запускаем двигатель')




Car.start_engine()

test_c = Car()

car_1 = Car(color='Red')
car_1.start_engine()
car_1.count_r

print(getattr(car_1, 'count_r')) # Передаем в функцию объект класса и название атрибута этого объекта
setattr(car_1, 'color', 'Dark') # Задаем значение атрибуту объекта класса

status = hasattr(car_1, 'count_r') # Проверка на наличие атрибута
print(status)

print(getattr(car_1, 'color'))
delattr(car_1, 'color') # Удаление атрибута объекта класса

# print(Car.__dict__)
# print(Car.__doc__)
# # print(Car.__class__.__dict__)
# print(dir(car_1))

# print(car_1.color)
car_1.count_r = 3 # Переопределение атрибутов объекта класса
# print(car_1.count_r)

car_2 = Car('Yellow')
car_3 = Car('Green')

# print(Car.color, test_c.count_r)
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
