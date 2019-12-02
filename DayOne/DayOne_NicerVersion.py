# Example of a cleaner and nicer solution

# Both version take arround .35 seconds to find both
# solutions.


def get_fuel(mass):
    return (int(mass) // 3) - 2

def get_fuel_recursive(mass):
    calculated_fuel = (int(mass) // 3) - 2
    if calculated_fuel < 0:
        return 0
    return calculated_fuel + get_fuel_recursive(calculated_fuel)


def main():
    lines = list(open('input.txt', 'r'))
    result_one = 0

    for line in lines:
        result_one += get_fuel(line)

    print("Day One Part One Solution: %d" % (result_one))

    result_two = 0

    for line in lines:
        result_two += get_fuel_recursive(line)

    print("Day One Part Two Solution: %d" % (result_two))


if __name__ == "__main__":
    main()