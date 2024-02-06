"""EX01 - Simple Battleship - A cute step toward Battleship."""
__author__ = "730621537"

locationof_boat = int(input("Pick a secret boat location between 1 and 4: "))
if not (1 <= locationof_boat <= 4):
    print(f"Error! {locationof_boat} too {'low' if locationof_boat < 1 else 'high'}!")
    exit()
guess = int(input("Guess a number between 1 and 4: "))
if not (1 <= guess <= 4):
    print(f"Error! {guess} too {'low' if guess < 1 else 'high'}!")
if guess == locationof_boat:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result = RED_BOX if guess == locationof_boat else WHITE_BOX
emoji_string = ""

box_number = 1
while box_number < 5:
    emoji_string += result if box_number == guess else BLUE_BOX
    box_number += 1

print(emoji_string)
if not (1 <= locationof_boat <= 4):
    if locationof_boat < 1:
        print(f"Error! {locationof_boat} too low!")
    else:
        print(f"Error! {locationof_boat} too high!")
    exit()

if not (1 <= guess <= 4):
    if guess < 1:
        print(f"Error! {guess} too low!")
    else:
        print(f"Error! {guess} too high!")
    exit()