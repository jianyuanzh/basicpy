import json

numbers = [1, 1, 2, 3, 5, 8, 13]

filename = 'numbers.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)
