import json
import character
import random

# Dialog

response = "\n>> "
return_to_menu = "Returning to Menu..."

def error(message):
    print("> Error:", message)

def dialog_simple(option1, option2):
    print(f"\n> [1]", option1)
    print(f"> [2]", option2)
    
def dialog_advanced(option1, option2, option3, option4):
    print(f"\n> [1]", option1)
    print(f"> [2]", option2)
    print(f"> [3]", option3)
    print(f"> [4]", option4)
    


# Saving and loading

# Saves character sheet to JSON
def save_game(player, inventory):
    print("Saving game...")
    sleep(1)
    save_character(player)
    print("Saving character data...")
    sleep(0.5)
    save_inventory(inventory)
    print("Saving inventory data...")
    sleep(0.5)
    print("Game saved!")

def save_character(player):
    character_data = {
        "Name": player.character_name,
        "Class": player.character_class,
        "Health": player.health,
        "Stamina": player.stamina,
        "Magic": player.magic,
        "Abilities": player.abilities
    }
    
    with open("character.json", "w") as f:
        json.dump(character_data, f, indent=4)

# Saves inventory to JSON
def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

# Saves current progress
def save_progress(progress):
    with open("progress.json", "w") as f:
        json.dump(progress, f, indent=4)

# Loads character from JSON
def load_character():
    file = "character.json"
    try:
        with open(file, "r") as f:
            content = f.read().strip()
            print(f"Reading {file}...")
            sleep(0.5)
            if not content:  # Check if the file is empty
                error("File is empty.")
                sleep(0.5)
                return None
            data = json.loads(content)  # Parse the JSON content
            print("Loading Character...")
            sleep(0.5)
            player = character.character(
                data["Name"], 
                data["Class"], 
            )
            
            player.health = data["Health"] 
            player.stamina = data["Stamina"] 
            player.magic = data["Magic"]
            player.abilities = data["Abilities"]
            
            print("Character loaded successfully!\n")
            sleep(1)
            return player
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return None

# Load inventory from JSON
def load_inventory():
    file = "inventory.json"
    try:
        with open(file, "r") as f:
            content = f.read().strip()
            print(f"Reading {file}...")
            sleep(0.5)
            if not content:
                error("File is empty.")
                return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}
            print("Loading Inventory...")
            sleep(0.5)
            print("Inventory loaded successfully!\n")
            sleep(1)
            return json.loads(content)
    except FileNotFoundError:
        return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}

# Load progress from JSON
def load_progress():
    file = "progress.json"
    try:
        with open(file, "r") as f:
            content = f.read().strip()
            print(f"Reading {file}...")
            sleep(1)
            if not content:
                error("File is empty. Starting a new game.")
                return None
            sleep(0.5)
            print("Progress loaded successfully!\n")
            sleep(1)
            return json.loads(content)
    except FileNotFoundError:
        print("Save file not found. Starting a new game...")
        return None
    except json.JSONDecodeError:
        print("Error reading save file. It may be corrupted.")
        return None





# Dice
def dice():
    number = random.randint(1,6)
    return number

def roll_die():
    print("\nRoll the Die!")
    print("> [r] Roll")
    
    roll = input(response)
    
    # Check if roll was legit
    if roll == "r":
        number = dice()
        sleep(1)
        print(f"You rolled {number}!\n")
        # Check roll strength
        if number >= 5:
            print("Critical success!")
        elif number <= 3:
            print("Critical faluire!")
        return number
    else:
        print(error("Unrecognised roll."))
        roll_dice()
    
    print("\n")

# Battles




# Animation
import time
import sys

def print_with_animation(text, delay=0.015):
    """Prints text character by character with a delay for animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after printing

def print_spacing():
    for i in range(0,50):
        print()

# Sleeps to make terminal printing nicer
def sleep(seconds):
    time.sleep(seconds)

# Next event animation
def next_event():
    sleep(1)
    print_spacing()