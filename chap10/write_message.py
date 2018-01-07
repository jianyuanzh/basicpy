file_name = 'programming.txt'

# r: read only
# w: writeable
# a: append in tail
with open(file_name, 'w') as file:
    file.write('This is a message from three body')


# write multi lines
with open('write_multiline.txt', 'w') as file:
    file.write('Hello world\n')
    file.write('good time\n')
    file.write('enjoy life\n')

# append to existing file
with open('append_existing_file.txt', 'a') as file:
    file.write('This is appended\n')
    file.write('This is appended again\n')