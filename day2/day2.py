EXAMPLE_SPREADSHEET = ("5 1 9 5\n"
                       "7 5 3\n"
                       "2 4 6 8\n")


def calc_checksum(spreadsheet):
    checksum = 0
    spreadsheet_rows = spreadsheet.strip().split("\n")
    for row in spreadsheet_rows:
        int_vals = [int(n) for n in row.split()]
        checksum += max(int_vals) - min(int_vals)
    return checksum


def main():
    assert calc_checksum(EXAMPLE_SPREADSHEET) == 18
    with open('input.txt', 'r') as input_file:
        input_spreadsheet = input_file.read()
        print(calc_checksum(input_spreadsheet))




if __name__ == "__main__":
    main()
