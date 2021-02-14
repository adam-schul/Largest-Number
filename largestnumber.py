
# Create empty list to be sorted later
l = []

# Ask the user for their list of numbers
print('Type a list of integers and press enter.', end=' ')

# Set empty string to a variable that will store each number
number1 = ''

sheep = input()

# Add spaces to end of user input to help program
sheep = sheep + '  '

# Break the user's input into chunks of just each number
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

# Sort the numbers by storing the largest in the 'largest' variable and comparing each value to it
for i in range(len(l)):
    if int(l[i]) > largest:
        largest = int(l[i])
    else:
        pass

# Print the result
print(largest)



