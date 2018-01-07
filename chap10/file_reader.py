with open('pi_digits.txt') as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())

print("\n\n")

# read per line

with open('pi_digits.txt') as pi_obj:
    for line in pi_obj:
        print(line.rstrip())

print("\n\n")

# use the file content
with open('pi_digits.txt') as file:
    pi_str = ''
    for line in file:
        pi_str += line.rstrip()

print(pi_str[:53] + '...')
print(len(pi_str))
