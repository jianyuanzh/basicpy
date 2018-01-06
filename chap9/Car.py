class Car:
    def __init__(self, make, model, year, olodmeter_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = olodmeter_reading  # 默认值

    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")


my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_descriptive())
my_new_car.read_odometer()

your_car = Car("BMW", 'x7', 2014, 600000)
print(your_car.get_descriptive())
your_car.read_odometer()
