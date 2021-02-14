

l = []




print('Type a list of integers and press enter.', end=' ')
number1 = ''

sheep = input()
sheep = sheep + '  '
for i in range(len(sheep)):
    if (sheep[i] == ' ' or sheep[i] == ',') and (sheep[i-1] == ' ' or sheep[i-1] == ','):
        pass
    elif sheep[0] == ' ' or sheep[0] == ',':
        pass
    elif (sheep[i] == ' ' or sheep[i] == ',') and (sheep[i-1] != ' ' or sheep[i-1] == ','):
        l.append(number1)
        number1 = ''
    else:
        number1 += sheep[i]
largest = 0

for i in range(len(l)):
    if int(l[i]) > largest:
        largest = int(l[i])
    else:
        pass

print(largest)



