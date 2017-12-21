squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# more simple solution

print([val ** 2 for val in range(1, 11)])
