import re


def count_overlap(list_of_claims):
    fabric = [["0" for i in range(1000)] for j in range(1000)]
    overlaps = 0
    for claim in range(len(list_of_claims)):
        temp_list = re.findall(r'-?\d+', list_of_claims[claim])
        claim_loc_x = int(temp_list[1])
        claim_loc_y = int(temp_list[2])
        claim_size_width = int(temp_list[3])
        claim_size_height = int(temp_list[4])

        for i in range(claim_size_width):
            for j in range(claim_size_height):
                space = fabric[claim_loc_x + i][claim_loc_y+j]
                if space == "0":
                    fabric[claim_loc_x + i][claim_loc_y+j] = "1"
                elif space == "1":
                    fabric[claim_loc_x + i][claim_loc_y+j] = "x"
                    overlaps += 1
    return overlaps


def main():
    # input_values = ["#1 @ 10,30: 40x40", "#2 @ 30,10: 40x40", "#3 @ 50,50: 20x20"]
    with open('day3input.txt') as f:
        input_values = f.readlines()
        answer = count_overlap(input_values)
        print(answer)


if __name__ == "__main__":
    main()
