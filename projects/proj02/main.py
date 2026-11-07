# Shakespeare Storytelling Game
# CS31 Python Project2
#Nazar Hammam 11/08/2026

def main():
    print("=" * 45)
    print("         WELCOME TO THE SHAKESPEARE GAME      ")
    print("=" * 45)

    # Game configuration and tracking defaults
    story_count = 0
    name = "Noble Traveler"  # Initialized globally to prevent a NameError if the user quits early

    # Ask the player if they want to play
    answer = input("\nWould you like to play a game? (y/n): ").lower()
    # Accounts for common spacing entries without using .strip()
    while answer != "y" and answer != "n" and answer != " y" and answer != "n ":
        print("Please enter y or n.")
        answer = input("Would you like to play a game? (y/n): ").lower()

        # Look for the core character input
    if "y" in answer:
        name = input("\nFirst, what is your name? ").title()
        if name == "":
            name = "Noble Traveler"
        print(f"\nHello, {name}! Let's have some fun with Shakespeare!")
        playing = True
    else:
        print("\nFarewell then, traveler!")
        playing = False

    while playing:
        print("\n" + "-" * 45)
        print("Choose the type of story you want to create:")
        print("1. A Funny Insult Story")
        print("2. A Wonderful Compliment Story")
        print("-" * 45)

        choice = input("Enter 1 or 2 (or 'q' to quit): ")
        # Check explicit strings instead of stripping whitespace
        while choice != "1" and choice != "2" and choice != "q" and choice != " 1" and choice != " 2" and choice != " q":
            print("That is not a valid choice. Try again.")
            choice = input("Please enter 1, 2, or 'q': ")

        if "q" in choice:
            playing = False
            print(f"\nFarewell, {name}! You created {story_count} stories today.")
            break

        if "1" in choice:
            # Story number 1: Shakespeare Insult
            print("\nLet's create a funny insult story!")
            character = input("Enter a person's name: ")
            animal = input("Enter an animal: ")
            food = input("Enter a type of food: ")
            adjective = input("Enter an adjective: ")
            clothing = input("Enter an item of clothing: ")
            place = input("Enter a place: ")
            drama = input("Choose a drama level from 1 to 10: ")
            action = input("Enter an action word: ")

            print("\n" + "=" * 45)
            print("             YOUR SHAKESPEARE INSULT          ")
            print("=" * 45)
            print(f"\nHear ye, hear ye! {character}, thou foolish {animal}!")
            print(f"Thy breath smells worse than old, rotten {food}!")
            print(f"Thou art so {adjective} that even thy own {clothing} rejects thee!")
            print(f"Flee to {place} immediately at a drama level of {drama},")
            print(f"lest we force thee to {action} in front of the entire court!")
            print("=" * 45)
            story_count += 1

        elif "2" in choice:
            # Story number 2: Shakespeare Compliment
            print("\nLet's create a wonderful compliment story!")
            character = input("Enter a person's name: ")
            celestial = input("Enter a celestial body (e.g., sun, star, moon): ")
            gem = input("Enter a gemstone: ")
            flower = input("Enter a flower: ")
            virtue = input("Enter a noble quality or virtue: ")
            instrument = input("Enter a musical instrument: ")

            print("\n" + "=" * 45)
            print("           YOUR SHAKESPEARE COMPLIMENT        ")
            print("=" * 45)
            print(f"\nSoft! What light through yonder window breaks?")
            print(f"It is the radiant {character}, whose eyes outshine the {celestial}!")
            print(f"Thy heart is as pure as a flawless {gem},")
            print(f"and thy presence is sweeter than a blooming {flower} in springtime.")
            print(f"With unmatched {virtue}, thy voice plays upon the soul like a sweet {instrument}.")
            print("=" * 45)
            story_count += 1

        # Ask if they want to play again
        play_again = input("\nWould you like to create another story? (y/n): ").lower()
        if "y" not in play_again:
            playing = False
            print(f"\nFarewell, {name}! You created {story_count} stories today.")


if __name__ == "__main__":
    main()
