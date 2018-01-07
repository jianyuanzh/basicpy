import json

filename = 'username.json'

try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as file:
        json.dump(username, file)
        print("We'll remeber you when you come back, " + username.title() + "!")
else:
    print("Welcome back " + username + "!")
