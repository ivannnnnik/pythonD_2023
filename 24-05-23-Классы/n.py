class Car:
    def start(self):
        print('start engine')
    def mute(self):
        print('mute engine')


class CargoCar(Car):
    def shipment(self):
        if self.age > 23:
            return True
        else:
            return False

car_1 = CargoCar()
car_1.start()
car_1.shipment()
car_1.mute()