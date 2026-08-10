# Read rows and starting number
rows = int(input())
starting_number = int(input())

second_number = starting_number

for row in range(1, rows + 1):
    # First row: print all numbers starting from starting_number
    if row == 1:
        each_row = ""
        for column in range(1, rows + 1):
            each_row = each_row + str(starting_number) + " "
            starting_number += 1
        print(each_row)

    # Last row: print the starting_number with leading spaces
    elif row == rows:
        each_row = " " * (2 * (row - 1))
        each_row = each_row + str(second_number) + " "
        print(each_row)

    # Middle rows: print boundaries and hollow spaces
    else:
        spaces = " " * (2 * (row - 1))
        hollow_spaces = " " * (2 * (rows - row) - 1)

        each_row = (
            spaces
            + str(second_number)
            + " "
            + hollow_spaces
            + str(second_number + rows - row)
            + " "
        )
        print(each_row)
