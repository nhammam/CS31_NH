# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 10/22/2026

import random

# print the title of the program
def display_title():
    print("Guess the Number game")
    print()

def play_game():
    print(
        """
E: Easy - Guess from 1 to 10, limit 5 attempts
M: Medium - Guess from 1 to 100, limit 7 attempts
H: Hard - Guess from 1 to 1000, limit 10 attempts
"""
    )
    
    your_level = input("Which level would you like to play? E/M/H: ")
    
    # set the limit and total allowed attempts based on their game level choice
    if your_level.upper() == "E":
        limit = 10
        attempts = 5
    elif your_level.upper() == "M":
        limit = 10
        attempts = 7
    elif your_level.upper() == "H":
        limit = 1000
        attempts = 10
    else:
        # punish them if they don't enter correct level :)
        limit = 10000
        attempts = 5

    secret_number = random.randint(1, limit)
    print(f"I am thinking of a number from 1 to {limit}\n")
    
    count = 1 # keep track of the total number of attempts
    
    while (guess := int(input("Your guess: "))) != secret_number:
        # check if they have any attempts left
        if count >= attempts:
          print("Sorry, you ran out of attempts!")
          break
            
        if guess < secret_number:
            print("Sorry, your guess is too low.")
        elif guess > secret_number:
            print("Sorry, your guess is too high.")
            
        count += 1 # increment the guess attempt counter
    else:
        print(f'Congratulate! you guessed it in {count}tries!\n')
        # if they guessed correctly (the while loop terminated because guess == secret_number)
        #print(f"Awesome! You guessed the number in {count} attempts!")

# --- Main Program Execution ---
def main():
# the main program driverdisplay_title()
  display_title()
#ask players name
  player_name = input("Hi there! What is your name? ")
  again = "y" # set inicail game loop variable
  print()
  while again.lower() == "y": # play the game
      play_game()
      again = input(f"Would you like to play another round of the game,{player_name}? y/n: ")
      print()
  print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
