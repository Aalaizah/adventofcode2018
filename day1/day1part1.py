def add(startingValue, valueToAdd):
    return startingValue + valueToAdd


def main():
    file = open("day1part1input.txt", 'r')
    inputValues = file.readlines()
    currentFrequency = 0
    for value in inputValues:
        currentFrequency = add(currentFrequency, int(value))

    print(currentFrequency)


if __name__ == "__main__":
    main()
