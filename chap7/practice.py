sandwich_orders = ['name1', 'name2', 'name3']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("Your sandwich " + sandwich + " is done!")
    finished_sandwiches.append(sandwich)

print("All sandwiches are done:" + str(finished_sandwiches))
