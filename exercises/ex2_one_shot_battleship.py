"""EX02 One Shot Battlship."""

__author__ = "730621537"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def print_grid(size: int, secret_row: int, secret_column: int, user_row: int, user_column: int) -> None:
    for row in range(1, size + 1):
        row_string = ""
        for col in range(1, size + 1):
            if row == secret_row and col == secret_column:
                row_string += RED_BOX
            elif row == user_row and col == user_column:
                row_string += WHITE_BOX
            else:
                row_string += BLUE_BOX
        print(row_string)

def main():
    # Constants
    GRID_SIZE = 4
    SECRET_ROW = 3
    SECRET_COLUMN = 2

    # Prompt the user for guesses
    while True:
        try:
            guess_row = int(input("Guess a row: "))
            if guess_row < 1 or guess_row > GRID_SIZE:
                raise ValueError(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again.")
            guess_col = int(input("Guess a column: "))
            if guess_col < 1 or guess_col > GRID_SIZE:
                raise ValueError(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again.")
            break
        except ValueError as ve:
            print(ve)

    # Check the guess and provide feedback
    if guess_row == SECRET_ROW and guess_col == SECRET_COLUMN:
        print("Hit!")
    elif guess_row == SECRET_ROW:
        print("Close! Correct row, wrong column.")
    elif guess_col == SECRET_COLUMN:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")

    # Print the grid
    print_grid(GRID_SIZE, SECRET_ROW, SECRET_COLUMN, guess_row, guess_col)

if __name__ == "__main__":
    main()