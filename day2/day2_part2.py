import itertools

EXAMPLE_SPREADSHEET = ("5 9 2 8\n"
                       "9 4 7 3\n"
                       "3 8 6 5\n")


def calc_checksum(spreadsheet):
    def pair_not_divide(pair):
        low, high = pair
        return high % low != 0

    checksum = 0
    spreadsheet_rows = spreadsheet.strip().split("\n")
    for row in spreadsheet_rows:
        int_vals = [int(n) for n in row.split()]
        int_vals.sort()
        val_combinations = itertools.combinations(int_vals, 2)
        divisible_vals = itertools.dropwhile(pair_not_divide, val_combinations)
        low, high = next(divisible_vals)
        checksum += high / low
    return int(checksum)


def main():
    assert calc_checksum(EXAMPLE_SPREADSHEET) == 9
    with open('input.txt', 'r') as input_file:
        input_spreadsheet = input_file.read()
        print(calc_checksum(input_spreadsheet))




if __name__ == "__main__":
    main()
