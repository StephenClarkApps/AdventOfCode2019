# Day Three

# two "wires"
# find the intersection point closest to the central port

# use the Manhattan distance for this measurement.
# if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3

import itertools

first_wire_points = [(0,0)]
second_wire_points = [(0,0)]
starting_position = (0,0)

# Parse the input lines
lines = list(open('input.txt', 'r'))
wire_one_movements = lines[0].split(',')
wire_two_movements = lines[1].split(',')


def generateFirstWirePoints():
    current_first_wire_end_position = (0,0)
    for movement in wire_one_movements:
        direction = movement[0]
        distance = int(movement[1:])

        if direction == 'R':
            if current_first_wire_end_position[0] < (current_first_wire_end_position[0] + distance + 1):
                sign = 1
            else:
                sign = -1

            for x_pos in range(current_first_wire_end_position[0], current_first_wire_end_position[0] + distance + 1, sign):
                first_wire_points.append((x_pos, current_first_wire_end_position[1]))
                # print ((x_pos, current_first_wire_end_position[1]))

            end = (current_first_wire_end_position[0] + distance, current_first_wire_end_position[1])
            current_first_wire_end_position = end

        elif direction == 'L':
            if current_first_wire_end_position[0] < (current_first_wire_end_position[0] - distance - 1):
                sign = 1
            else:
                sign = -1

            for x_pos in range(current_first_wire_end_position[0], current_first_wire_end_position[0] - distance - 1, sign):
                first_wire_points.append((x_pos, current_first_wire_end_position[1]))

            end = (current_first_wire_end_position[0] - distance , current_first_wire_end_position[1])
            current_first_wire_end_position = end
        elif direction == 'U':

            if current_first_wire_end_position[1] < (current_first_wire_end_position[1] + distance + 1):
                sign = 1
            else:
                sign = -1

            for y_pos in range(current_first_wire_end_position[1], current_first_wire_end_position[1] + distance + 1, sign):
                first_wire_points.append((current_first_wire_end_position[0], y_pos))

            end = (current_first_wire_end_position[0], current_first_wire_end_position[1] + distance)
            current_first_wire_end_position = end
        elif direction == 'D':
            if current_first_wire_end_position[1] < (current_first_wire_end_position[1] - distance - 1):
                sign = 1
            else:
                sign = -1

            for y_pos in range(current_first_wire_end_position[1], current_first_wire_end_position[1] - distance - 1, sign):
                first_wire_points.append((current_first_wire_end_position[0], y_pos))

            end = (current_first_wire_end_position[0], current_first_wire_end_position[1] - distance)
            current_first_wire_end_position = end


def generateSecondWirePoint():
    current_second_wire_end_position = (0,0)
    for movement in wire_two_movements:
        direction = movement[0]
        distance = int(movement[1:])

        if direction == 'R':
            if current_second_wire_end_position[0] < (current_second_wire_end_position[0] + distance + 1):
                sign = 1
            else:
                sign = -1

            for x_pos in range(current_second_wire_end_position[0], current_second_wire_end_position[0] + distance + 1, sign):
                second_wire_points.append((x_pos, current_second_wire_end_position[1]))

            end = (current_second_wire_end_position[0] + distance, current_second_wire_end_position[1])
            current_second_wire_end_position = end

        elif direction == 'L':
            if current_second_wire_end_position[0] < (current_second_wire_end_position[0] - distance - 1):
                sign = 1
            else:
                sign = -1

            for x_pos in range(current_second_wire_end_position[0], current_second_wire_end_position[0] - distance - 1, sign):
                second_wire_points.append((x_pos, current_second_wire_end_position[1]))

            end = (current_second_wire_end_position[0] - distance , current_second_wire_end_position[1])
            current_second_wire_end_position = end
        elif direction == 'U':

            if current_second_wire_end_position[1] < (current_second_wire_end_position[1] + distance + 1):
                sign = 1
            else:
                sign = -1

            for y_pos in range(current_second_wire_end_position[1], current_second_wire_end_position[1] + distance + 1, sign):
                second_wire_points.append((current_second_wire_end_position[0], y_pos))

            end = (current_second_wire_end_position[0], current_second_wire_end_position[1] + distance)
            current_second_wire_end_position = end
        elif direction == 'D':
            if current_second_wire_end_position[1] < (current_second_wire_end_position[1] - distance - 1):
                sign = 1
            else:
                sign = -1

            for y_pos in range(current_second_wire_end_position[1], current_second_wire_end_position[1] - distance - 1, sign):
                second_wire_points.append((current_second_wire_end_position[0], y_pos))

            end = (current_second_wire_end_position[0], current_second_wire_end_position[1] - distance)
            current_second_wire_end_position = end

      
def common_members(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return(a_set & b_set) 
    else: 
        return []

generateFirstWirePoints()
generateSecondWirePoint()
common_points = common_members(first_wire_points, second_wire_points)

min_distance = 99999999999
for point in common_points:
    if (abs(point[0]) + abs(point[1]) < min_distance) & (abs(point[0]) + abs(point[1]) != 0):
        min_distance = abs(point[0]) + abs(point[1])

print (min_distance)

