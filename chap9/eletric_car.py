class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def getDescriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_oldmeter(self):
        print("This car has " + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increase_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car's gas task is filled now")

class Battery:
    def __init__(self):
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery')



class EletricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    def fill_gas_tank(self):
        print('This car has no gas tank')


my_tesla = EletricCar('tesla', 'model s', 2016)

print(my_tesla.getDescriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
