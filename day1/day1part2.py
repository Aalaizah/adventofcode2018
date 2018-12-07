def loopThroughFrequencies(frequencyList):
    currentFrequency = 0
    listOfFrequencies = []
    duplicateFound = False
    for value in frequencyList:
        currentFrequency = add(currentFrequency, int(value))
        if currentFrequency in listOfFrequencies:
            print(currentFrequency)
            duplicateFound = True
            return duplicateFound

        listOfFrequencies.append(currentFrequency)



def add(startingValue, valueToAdd):
    return startingValue + valueToAdd


def main():
    currentFrequency = 0
    dupeFound = False
    listOfFrequencies = [currentFrequency]

    while not dupeFound:
        with open('day1part1input.txt') as f:
            for line in f:
                currentFrequency += int(line)
                if currentFrequency in listOfFrequencies:
                    print(currentFrequency)
                    dupeFound = True
                    break
                listOfFrequencies.append(currentFrequency)


def old():
    file = open("day1part1input.txt", 'r')
    inputValues = file.readlines()
    dupeFrequency = False
    count = 0
    while not dupeFrequency:
        print(count)
        dupeFrequency = loopThroughFrequencies(inputValues)
        count += 1


if __name__ == "__main__":
    main()
