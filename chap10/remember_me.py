import json

username = input('What is your name?')

filename = 'username.json'
with open(filename, 'w') as file:
    json.dump(username, file)
    print("We'll remeber you when you come back, " + username.title() + "!")
