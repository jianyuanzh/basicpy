class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业！")

    def describe(self):
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " type restaurant")


shujin = Restaurant('Shujin', 'huge')
shujin.describe()
shujin.open_restaurant()
