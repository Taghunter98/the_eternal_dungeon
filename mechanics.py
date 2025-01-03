import json
import character
import random
import enemy

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
    sleep(0.5)
    save_inventory(inventory)
    sleep(0.5)
    #print("Game saved!")

def save_character(player):
    character_data = {
        "Name": player.character_name,
        "Class": player.character_class,
        "Health": player.health,
        "Base Health": player.base_health,
        "Base Damage": player.base_damage,
        "Stamina": player.stamina,
        "Magic": player.magic,
        "Abilities": player.abilities,
        "Ability Damage": player.ability_damage
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
            # print(f"Reading {file}...")
            if not content:  # Check if the file is empty
                error("File is empty.")
                sleep(0.5)
                return None
            data = json.loads(content)  # Parse the JSON content
            player = character.character(
                data["Name"], 
                data["Class"], 
            )
            
            # Load player info
            player.health = data["Health"]
            player.base_health = data["Base Health"]
            player.base_damage = data["Base Damage"]
            player.stamina = data["Stamina"] 
            player.magic = data["Magic"]
            player.abilities = data["Abilities"]
            player.ability_damage = data["Ability Damage"]
            
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
            # print(f"Reading {file}...")
            if not content:
                error("File is empty.")
                return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}
            # print("Loading Inventory...")
            # print("Inventory loaded successfully!\n")
            return json.loads(content)
    except FileNotFoundError:
        return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}

# Load progress from JSON
def load_progress():
    file = "progress.json"
    try:
        with open(file, "r") as f:
            content = f.read().strip()
            # print(f"Reading {file}...")
            if not content:
                save_progress("Level 1")
                return 
            sleep(0.5)
            # print("Progress loaded successfully!\n")
            return json.loads(content)
    except json.JSONDecodeError:
        print("Error reading save file. It may be corrupted.")
        return None





# Dice
def dice():
    number = random.randint(1,6)
    return number

def roll_die():
    print("\n+-------------------------------------------+")
    print("|               Roll The Dice               |")
    print("+-------------------------------------------+")
    print("> [r] Roll")
    
    roll = input(response)
    
    # Check if roll was legit
    if roll == "r":
        number = dice()
        sleep(1)
        print(f"\nYou rolled {number}!\n")
        # Check roll strength
        if number >= 5:
            print("Critical success!\n")
        elif number <= 2:
            print("Critical failure!\n")
        return number
    else:
        print(error("Unrecognised roll."))
        roll_dice()
    
    print("\n")




# Battles

def battle(player, inventory):
    print("\nYou have encountered an enemy!")
    dialog_simple("Ready yourself for battle!", "Try to flee")
    
    # Player input
    choice = input(response)
    
    # Battle logic
    battle_logic(choice, player, inventory)
    


def battle_logic(choice, player, inventory):
    
    # Check if choice is valid
    if choice == "1":
        # Select opponent
        get_enemy = select_enemy()
        entity = enemy.enemy_check(get_enemy)
        turn = 0
        
        # Main battle logic
        while entity.health > 0:
            
            # Print spacing for each turn
            print_spacing()
            
            turn += 1
            print_battle_turn(turn, player, entity)
            
            # Damage from enemy
            damage = enemy.attack_amount(entity.name)
            
            player.health -= damage
            print(f"You took {damage} damage!")
            
            # Check player health
            if character.check_health(player, inventory) is True:
                return
            else:
                sleep(2)
            
                # Damage from player
                player_damage = player_attack(player)
            
                # Calculate player damage
                print(f"\n{entity.name} took {player_damage} damage!")
                entity.health -= player_damage
                sleep(2)
        
        if entity.health <= 0:
            loot = entity.gold
            inventory["Gold"] += loot
            print(f"\nYou killed the {entity.name} and looted {loot} Gold!\n")
            save_game(player, inventory)
            return
    elif choice == "2":
        flee_chance = roll_die()
        if flee_chance > 4:
            print("\nYou mangage to flee without harm, this time...")
            return
        elif flee_chance < 4 and flee_chance > 2:
            print("The enemy manages to get a hit on you as you flee!\nYou took 10 damage!")
            player.health -= 10
        else:
            print("The enemy stabs you in the back as you flee!\nYou took 20 damage!")
            player.health -= 20
        
        # Check if player is dead
        if character.check_health(player, inventory) is True:
            return
        else:
            return
        
    else:
        error("Invalid input.")
        battle_logic(choice, player, inventory)
        
        
def player_attack(player):
    
    print_player_title(player)
    sleep(1)
    print("Choose Your Attack Type")
    dialog_simple("Strike with your main weapon", f"Unleash a powerful ability [{player.ability_counter} available]")
    choice = input(response)
    
    if choice == "1":
        damage = dice()
        print(f"\nYou roll {damage}.")
        player_base_damage = player.base_damage
        
        if damage > 2:
            return player_base_damage
    
        elif damage == 6:
            print("\nCritical hit!")
            return (player_base_damage + 5)
        else:
            print("\nEnemy dodged the attack!")
            return 0
    elif choice == "2":
        if player.ability_counter == 0:
            print("You are out of abilities!")
            return 0
        else:
            damage = ability_attack(player)
            print(f"\nYou use a powerful ability dealing {damage} damage!")
            player.ability_counter -= 1
            return damage
    else:
        error("Invalid input.")
        print("\nYou stand still and waste your turn...")
        return 0

def ability_attack(player):
    print("\nWhich ability would you like to use?")
    # Display all abilities to player
    abilities = player.abilities
    damage = player.ability_damage
    
    for ability in abilities:
        print(f"[{abilities.index(ability) + 1}] {ability}")
    
    choice = input(response)
    
    if choice == "1":
        return damage
    elif choice == "2":
        return damage
    else:
        error("Invalid input.")
        ability_attack(player)
    
def select_enemy():
    # Select enemy at random
    enemies = {
        1: "Goblin",
        2: "Ork",
        3: "Skeleton",
        4: "Troll",
        5: "Warg",
        6: "Armoured Ork",
        7: "Shadow Knight"
    }
    
    save = load_progress()
    
    next_enemy = 1
    
    if save in  ["first_battle", "Level 2"]:
        next_enemy = random.randint(1,3)
    elif save == "level_two_boss":
        next_enemy = 4
    elif save == "Level 3":
        next_enemy = random.randint(1,7)
    
    if next_enemy in enemies:
        print(enemies.get(next_enemy)) # debug
        return enemies.get(next_enemy)
    else:
        error("Unable to find enemy.")


def print_battle_turn(turn, player, entity):
    battle_text = f"""
+-------------------------------------------+
|               ~ TURN {turn} ~                  |
+-------------------------------------------+
 {player.character_name}  HP: {player.health}  |  {entity.name}  HP: {entity.health}
+-------------------------------------------+"""
    print_with_animation(battle_text)

def print_player_title(player):
    text = f"""\n
+-------------------------------------------+
 {player.character_name}'s Turn!                      
+-------------------------------------------+
"""
    print(text)

def print_enemy_title(entity):
    text = f"""\n
+-------------------------------------------+
 {entity.name}'s Turn!                      
+-------------------------------------------+
"""
    print(text)

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