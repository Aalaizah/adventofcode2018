from collections import Counter


def count_dupes(list_to_check, num_dupes_to_check):
    count = 0
    dupe_found = False
    for item in list_to_check:
        counter = Counter(item)
        for letter in counter:
            if counter[letter] == num_dupes_to_check:
                dupe_found = True
        if dupe_found:
            count += 1
        dupe_found = False

    return count


def main():
    with open('day2input.txt') as f:
        input_values = f.readlines()
        exactly2 = count_dupes(input_values, 2)
        exactly3 = count_dupes(input_values, 3)
        print(exactly2 * exactly3)


if __name__ == "__main__":
    main()
