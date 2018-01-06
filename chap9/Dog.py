class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting. ")

    def roll_over(self):
        print(self.name.title() + " is now rolled over! ")


duoduo = Dog('duoduo', 1)
duoduo.sit()
duoduo.roll_over()

print(duoduo.name.title())
print(str(duoduo.age))
