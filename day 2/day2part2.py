def find_id(list_to_check):
    second_list_to_check = list_to_check[1:]
    for item in list_to_check:
        num_of_discrepancies = 0
        current_test = item
        for item2 in second_list_to_check:
            index_of_discrepancy = -1
            index = 0
            for letter1, letter2 in zip(current_test, item2):
                if letter1 != letter2:
                    num_of_discrepancies += 1
                    index_of_discrepancy = index
                if num_of_discrepancies > 1:
                    break
                index += 1
            if num_of_discrepancies == 1:
                return current_test[:index_of_discrepancy] + current_test[index_of_discrepancy+1:]
            num_of_discrepancies = 0


def main():
    with open('day2input.txt') as f:
        input_values = f.readlines()
        answer = find_id(input_values)
        print(answer)


if __name__ == "__main__":
    main()
