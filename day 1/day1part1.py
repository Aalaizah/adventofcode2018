def add(starting_value, value_to_add):
    return starting_value + value_to_add


def main():
    file = open("day1part1input.txt", 'r')
    input_values = file.readlines()
    current_frequency = 0
    for value in input_values:
        current_frequency = add(current_frequency, int(value))

    print(current_frequency)


if __name__ == "__main__":
    main()
