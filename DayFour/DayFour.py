# Day Four

lines = list(open('input.txt', 'r'))
input_range = lines[0].split('-')

lower_bound = int(input_range[0])
upper_bound = int(input_range[1])

# possible_answers = []

def hasTwoTheSameInARow(a):
    last_char = ''
    for char in str(a):
        if char == last_char:
            return True
        last_char = char
    return False

def neverDecreases(b):
    last_char = -1
    for char in str(b):
        if int(char) < int(last_char):
            return False
        last_char = char
    return True

counter = 0
for password in range(lower_bound, upper_bound + 1):
    #possible_answers.append(password)
    if hasTwoTheSameInARow(password) & neverDecreases(password):
        #print (password)
        counter += 1


print (counter)