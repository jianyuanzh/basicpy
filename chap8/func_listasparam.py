def show_magicians(magicians):
    for i in range(len(magicians)):
        magicians[i] = make_great(magicians[i])
    print("The changed list: " + str(magicians))


def make_great(magician):
    return 'The great ' + magician.title()


magicians = ['David', 'Tommy', 'Newbi']
show_magicians(magicians[:])
print('The original list: ' + str(magicians))
