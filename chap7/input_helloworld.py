
msg = input('Tell me your name:')
print('Hello, ' + msg.title())
input_age = input('How old are you?')

age = int(input_age)

if age > 18:
    print('You can enter the club, ' + msg.title())
else:
    print('You are too young to get in, boy')
