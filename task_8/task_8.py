read_file = ''

with open('123.txt', 'r') as file:
    read_file = file.read()

with open('321.txt', 'w') as file:
    read_file = read_file[-1::-1]
    file.write(read_file)

with open('123.txt', 'r') as file:
    read = file.read()
    print(read)

with open('321.txt', 'r') as file:
    read = file.read()
    print(read)




