"""EX02 One Shot Battlship."""

__author__ = "730621537"

BLUE_BOX: str = "🟦"
RED_BOX: str = "🟥"
WHITE_BOX: str = "⬜"

grid_size = 4
secret_row = 3
secret_column = 2

print("Guess a row:", end=" ")
guess_row = int(input())
while guess_row < 1 or guess_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_row = int(input())

print("Guess a column:", end=" ")
guess_column = int(input())
while guess_column < 1 or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_column = int(input())

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")

result_box = RED_BOX if guess_row == secret_row and guess_column == secret_column else WHITE_BOX

row_counter = 1
for row in range(1, grid_size + 1):
    emoji_row = ""
    for column in range(1, grid_size + 1):
        if row == guess_row and column == guess_column:
            if row == secret_row and column == secret_column:
                emoji_row += RED_BOX  
            else:
                emoji_row += result_box  
        else:
            emoji_row += BLUE_BOX  
    row_counter += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")