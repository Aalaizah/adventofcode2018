import re


def count_overlap(list_of_claims):
    fabric = [["0" for i in range(1000)] for j in range(1000)]
    overlapped_claims = [False] * len(list_of_claims)
    claim_info = []
    non_overlapped_claim = -1
    for claim in range(len(list_of_claims)):
        temp_list = re.findall(r'-?\d+',list_of_claims[claim])
        claim_id = int(temp_list[0])
        claim_loc_x = int(temp_list[1])
        claim_loc_y = int(temp_list[2])
        claim_size_width = int(temp_list[3])
        claim_size_height = int(temp_list[4])
        claim_info.append([claim_id, claim_loc_x, claim_loc_y, claim_size_width, claim_size_height])

        for i in range(claim_size_width):
            for j in range(claim_size_height):
                space = fabric[claim_loc_x + i][claim_loc_y+j]
                if space == "0":
                    fabric[claim_loc_x + i][claim_loc_y+j] = "1"
                elif space == "1":
                    fabric[claim_loc_x + i][claim_loc_y+j] = "x"
                    overlapped_claims[claim_id-1] = True

    for claim in range(len(claim_info)):
        current_claim = claim_info[claim]
        for i in range(current_claim[3]):
            for j in range(current_claim[4]):
                space = fabric[current_claim[1] + i][current_claim[2] + j]
                if space == "x":
                    overlapped_claims[current_claim[0]-1] = True
        if not overlapped_claims[current_claim[0]-1]:
            non_overlapped_claim = current_claim[0]
            break

    return non_overlapped_claim


def main():
    # input_values = ["#1 @ 10,30: 40x40", "#2 @ 30,10: 40x40", "#3 @ 50,50: 20x20"]
    with open('day3input.txt') as f:
        input_values = f.readlines()
        answer = count_overlap(input_values)
        print(answer)


if __name__ == "__main__":
    main()