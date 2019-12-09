# Day Two
something = True
# create an array of machine codes
machine_codes = []

# Process input into list of integers
lines = list(open('input.txt', 'r'))
string = lines[0]
array_of_codes_str = string.split(',')
array_of_codes = [int(i) for i in array_of_codes_str] 

reset_to = array_of_codes

def add(one_position):
    result = array_of_codes[array_of_codes[one_position + 1]] + array_of_codes[array_of_codes [one_position + 2]]
    array_of_codes[array_of_codes[one_position + 3]] = result

# on encountering a 2 we do the above but multiply
def multiply(two_position):
    result = array_of_codes[array_of_codes[two_position + 1]] * array_of_codes[array_of_codes [two_position + 2]]
    array_of_codes[array_of_codes[two_position + 3]] = result


def execute(position):
    global something
    if position > len(array_of_codes):
        print("out of range ??")
        something = False

    if array_of_codes[position] == 1:
        add(position)
    elif array_of_codes[position] == 2:
        multiply(position)
    elif array_of_codes[position] == 3:
        print("Op Code 3")
    elif array_of_codes[position] == 4:
        print("Op Code 4")
    elif array_of_codes[position] == 99:
        #halt program
        print("HALT: ")
        print (array_of_codes[0])
        something = False
        # quit() # Don't quit but stop loop ?!?!?

array_of_codes[1] = 12
array_of_codes[2] = 2

current_position = 0

while something == True:
    execute(current_position)
    current_position += 4



for verb in range (0, 100):
    for noun in range (0, 100):
        array_of_codes = reset_to
        array_of_codes[1] = noun
        array_of_codes[2] = verb
        current_position = 0
        something = True
        while something == True:
            execute(current_position)
            current_position += 4


