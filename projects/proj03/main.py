# Starting file for PROJECT 3
# Title: Character Generator & Attack on Titan RPG
# Name: Nazar, November 21, 2026, CS 31 - Python
# Part 1 creates random fantasy characters and prints a character sheet.
# Part 2 launches the Attack on Titan RPG where you create a Scout Regiment
# character, get assigned a Titan and stats, and battle random AoT enemies.

import random

# Part 1: Fantasy Character Generator lists
fantasy_stats_list = ["HP", "Strength", "Wisdom", "Dexterity", "Charisma", "Constitution"]
fantasy_names = ["Thorin", "Elara", "Grimlock", "Seraphine", "Borin", "Lyra"]

# Part 2: Attack on Titan RPG lists
aot_stats_list = ["Hit points", "Balance", "Strength", "Stamina", "Speed"]
aot_names = ["Amilyn", "Eren", "Mikasa", "Armin", "Levi", "Jean"]
enemy_names = ["Bertholdt Hoover", "Reiner Braun", "Annie Leonhart", "Zeke Yeager", "Porco Galliard"]
enemy_titans = ["Collossal Titan", "Armored Titan", "Female Titan", "Beast Titan", "Jaw Titan"]


# --- PART 1 FUNCTIONS (Fantasy Character Generator) ---

def roll_fantasy_stat(stat_name):
    if stat_name == "HP":
        return random.randint(10, 30)
    return random.randint(3, 18)


def pick_race():
    number = random.randint(1, 5)
    if number == 1:
        return "Human"
    elif number == 2:
        return "Elf"
    elif number == 3:
        return "Dwarf"
    elif number == 4:
        return "Half-orc"
    else:
        return "Halfling"


def pick_class():
    number = random.randint(1, 5)
    if number == 1:
        return "Warrior"
    elif number == 2:
        return "Wizard"
    elif number == 3:
        return "Cleric"
    elif number == 4:
        return "Rogue"
    else:
        return "Orc"


def show_fantasy_character(name, race, character_class, stat_values):
    print("~*~*~Character Sheet~*~*~")
    print("Name: ", name)
    print("Race: ", race)
    print("Class:", character_class)

    for i in range(len(fantasy_stats_list)):
        label = fantasy_stats_list[i] + ":"
        print(f"{label:<14} {stat_values[i]}")

    print("====================")


def run_character_generator():
    print("~~~~~*~~~*~~~~~*~~~*~~~~~*~~~*")
    print("|Random Character Generator! |")
    print("~~~~~*~~~*~~~~~*~~~*~~~~~*~~~*\n")

    again = "y"
    while again == "y":
        char_name = input("What name would you like to use for your character?: ").strip()
        if char_name == "":
            char_name = random.choice(fantasy_names)

        stat_values = []
        for stat in fantasy_stats_list:
            stat_values.append(roll_fantasy_stat(stat))

        race = pick_race()
        character_class = pick_class()
        show_fantasy_character(char_name, race, character_class, stat_values)

        again = input("Would you like to generate a new character (y/n): ").strip().lower()
        print()

    print("Thanks for playing!\n")


# --- PART 2 FUNCTIONS (Attack on Titan RPG) ---

def roll_aot_stat(stat_name):
    if stat_name == "Hit points":
        return random.randint(70, 100)
    return random.randint(1, 10)


def pick_titan():
    number = random.randint(1, 5)
    if number == 1:
        return "Armored Titan"
    elif number == 2:
        return "Attack Titan"
    elif number == 3:
        return "Female Titan"
    elif number == 4:
        return "Beast Titan"
    else:
        return "Jaw Titan"


def create_aot_stats():
    values = []
    for stat in aot_stats_list:
        values.append(roll_aot_stat(stat))
    return values


def show_aot_character(name, titan, stat_values):
    print(f"\nWe have generated stats for your character, {name}. They are listed below:\n")
    print(f"Titan: {titan}\n")

    for i in range(len(aot_stats_list)):
        print(f"{aot_stats_list[i]}: {stat_values[i]}")

    print()


def show_battle_status(player_name, player_titan, player_stats, enemy_name, enemy_titan, enemy_stats):
    print("*****************************\n")
    print("           BATTLE\n\n")
    print(f"Enemy: {enemy_name}\n")
    print(f"Titan: {enemy_titan}\n")
    print(f"HP: {enemy_stats[0]}")
    print(f"Balance: {enemy_stats[1]}")
    print(f"Strength: {enemy_stats[2]}")
    print(f"Stamina: {enemy_stats[3]}")
    print(f"Speed: {enemy_stats[4]}\n\n")
    print(f"You: {player_name}\n")
    print(f"Titan: {player_titan}\n")
    print(f"HP: {player_stats[0]}")
    print(f"Balance: {player_stats[1]}")
    print(f"Strength: {player_stats[2]}")
    print(f"Stamina: {player_stats[3]}")
    print(f"Speed: {player_stats[4]}\n")
    print("*****************************\n")


def calculate_damage(attacker_stats, defender_stats):
    # index 1 = Balance, index 2 = Strength, index 4 = Speed
    base_damage = attacker_stats[2] * 3 + attacker_stats[4]
    defense = defender_stats[1] // 2
    damage = base_damage - defense
    if damage < 5:
        damage = 5
    return damage


def run_battle(player_name, player_titan, base_player_stats):
    # copy the list so each battle starts at full HP
    player_stats = list(base_player_stats)

    enemy_index = random.randint(0, len(enemy_names) - 1)
    enemy_name = enemy_names[enemy_index]
    enemy_titan = enemy_titans[enemy_index]
    enemy_stats = create_aot_stats()

    while player_stats[0] > 0 and enemy_stats[0] > 0:
        show_battle_status(
            player_name, player_titan, player_stats,
            enemy_name, enemy_titan, enemy_stats
        )

        damage_to_enemy = calculate_damage(player_stats, enemy_stats)
        damage_to_player = calculate_damage(enemy_stats, player_stats)

        enemy_stats[0] -= damage_to_enemy
        player_stats[0] -= damage_to_player

    if player_stats[0] <= 0 and enemy_stats[0] <= 0:
        print("Tie! Both Knocked out.\n")
    elif enemy_stats[0] <= 0:
        print(f"Victory! You defeated {enemy_name}!\n")
    else:
        print(f"Defeat! {enemy_name} knocked you out!\n")

    print(f"Your Remaining HP: {player_stats[0]}")
    print(f"Enemy Remaining HP: {enemy_stats[0]}\n")


def run_aot_rpg():
    print("Welcome to the Attack on Titan RPG game!\n")
    start_game = input("Would you like to create a character to start the game? y/n : ").strip().lower()

    if start_game != "y":
        print("\nThanks for playing!")
        return

    char_name = input("\nWhat would you like to name your character? : ").strip()
    if char_name == "":
        char_name = random.choice(aot_names)

    print(f"\nWelcome to the Scout Regiment, {char_name}.")

    player_titan = pick_titan()
    player_stats = create_aot_stats()
    show_aot_character(char_name, player_titan, player_stats)

    battle_choice = input("Would you like to battle an AoT character? y/n : ").strip().lower()
    print()

    while battle_choice == "y":
        run_battle(char_name, player_titan, player_stats)
        battle_choice = input("Would you like to battle a different character? y/n : ").strip().lower()
        print()

    print("Thanks for playing!")


def main():
    run_character_generator()
    run_aot_rpg()


if __name__ == "__main__":
    main()

