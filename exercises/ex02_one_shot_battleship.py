"""EX02 One Shot Battlship."""

__author__ = "730621537"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def main():
    grid_size = 4
    secret_row = 3
    secret_column = 2
    
    guess_row = int(input("Guess a row: "))
    guess_column = int(input("Guess a column: "))

    if guess_row == secret_row and guess_column == secret_column:
        print("Hit!")
    elif (guess_row < 1 or guess_row > grid_size) or (guess_column < 1 or guess_column > grid_size):
        print("Out of bounds!")
    else:
        print("Miss!")
    
    row_counter = 1
    while row_counter <= grid_size:
        row_string = ""
        column_counter = 1
        while column_counter <= grid_size:
            if guess_row == row_counter and guess_column == column_counter:
                if guess_row == secret_row and guess_column == secret_column:
                    row_string += RED_BOX
                else:
                    row_string += WHITE_BOX
            else:
                row_string += BLUE_BOX
            column_counter += 1
        print(row_string)
        row_counter += 1

if __name__ == "__main__":
    main()
    
