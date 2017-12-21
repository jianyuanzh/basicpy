my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

print("my foods: " + str(my_foods))
print("friend's foods: " + str(friend_foods))

my_foods.pop(2)
print("my foods (carrot removed): " + str(my_foods))
print("friend's foods: " + str(friend_foods))

