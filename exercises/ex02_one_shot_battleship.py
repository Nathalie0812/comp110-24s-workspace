"""EX02 One Shot Battlship."""

__author__ = "730621537"

BLUE_BOX: str = "🟦"
RED_BOX: str = "🟥"
WHITE_BOX: str = "⬜"

grid_size = 4
secret_row = 3
secret_column = 2

print(f"Guess a row: ", end="")
guess_row = int(input())
while guess_row < 1 or guess_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_row = int(input())

print(f"Guess a column: ", end="")
guess_column = int(input())
while guess_column < 1 or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_column = int(input())

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")

# Print the grid after the guess
for row_counter in range(1, grid_size + 1):
    emoji_row = ""
    for column_counter in range(1, grid_size + 1):
        if row_counter == guess_row and column_counter == guess_column:
            emoji_row += WHITE_BOX
        elif row_counter == secret_row and column_counter == secret_column:
            emoji_row += RED_BOX
        else:
            emoji_row += BLUE_BOX
    print(emoji_row)