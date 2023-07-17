import numpy as np

def solve_sudoku(sudoku):
    if not find_empty_cell(sudoku):
        return True

    row, col = find_empty_cell(sudoku)

    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
            sudoku[row][col] = num

            if solve_sudoku(sudoku):
                return True

            sudoku[row][col] = 0

    return False

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if sudoku[box_row + i][box_col + j] == num:
                return False

    return True

def find_empty_cell(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

# Prompt the user to enter the Sudoku grid
print("Please enter the Sudoku grid (9 rows, each row without spaces):")
sudoku = []
for i in range(9):
    row = list(input("Enter the elements of row {} without any spaces: ".format(i+1)))
    row = [int(i) for i in row]
    sudoku.append(row)

print("Original Sudoku Grid:")
print(np.matrix(sudoku))
print()

if solve_sudoku(sudoku):
    print("Solution:")
    print(np.matrix(sudoku))
else:
    print("No solution exists for the given Sudoku grid.")

