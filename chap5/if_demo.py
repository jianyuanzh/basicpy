cars = ['audi', 'bmw', 'great wall', 'subaru', 'toyota']

for car in cars:
    if car.upper() == 'audi'.upper():
        print("This is " + car.upper())
    elif (car.lower() != 'great waLL'.lower()) and (car.lower() != 'shabi'.lower()):
        print("Not audi or great wall, but " + car.upper())
    else:
        print('Not audi but ' + car.upper())


print('car' == 'car')
print('car' == 'bike')