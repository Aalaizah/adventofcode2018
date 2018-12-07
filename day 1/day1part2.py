def main():
    current_frequency = 0
    dupe_found = False
    list_of_frequencies = [current_frequency]

    while not dupe_found:
        with open('day1part1input.txt') as f:
            for line in f:
                current_frequency += int(line)
                if current_frequency in list_of_frequencies:
                    print(current_frequency)
                    dupe_found = True
                    break
                list_of_frequencies.append(current_frequency)


if __name__ == "__main__":
    main()
