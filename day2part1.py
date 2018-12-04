from collections import Counter


def countdupes(listToCheck, numDupesToCheck):
    count = 0
    dupeFound = False
    for item in listToCheck:
        counter = Counter(item)
        for letter in counter:
            if counter[letter] == numDupesToCheck:
                dupeFound = True
        if dupeFound:
            count += 1
        dupeFound = False

    return count


def main():
    with open('day2input.txt') as f:
        inputValues = f.readlines()
        exactly2 = countdupes(inputValues, 2)
        print(exactly2)
        exactly3 = countdupes(inputValues, 3)
        print(exactly3)
        print(exactly2 * exactly3)


if __name__ == "__main__":
    main()
