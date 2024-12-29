import json
import character

# Dialog

response = "\n>> "

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
    save_character(player)
    save_inventory(inventory)

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
    try:
        with open("character.json", "r") as f:
            content = f.read().strip()  # Read the file and remove whitespace
            if not content:  # Check if the file is empty
                return None
            data = json.loads(content)  # Parse the JSON content
            player = character.character(
                data["Name"], 
                data["Class"], 
            )
            
            player.health = data["Health"] 
            player.stamina = data["Stamina"] 
            player.magic = data["Magic"]
            player.abilities = data["Abilities"]
            
            return player
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return None

# Load inventory from JSON
def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            content = f.read().strip()
            if not content:
                return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}
            return json.loads(content)
    except FileNotFoundError:
        return {"Gold": 0, "Weapons": [], "Armour": [], "Potions": [], "Quest Items": []}

# Load progress from JSON
def load_progress():
    try:
        with open("progress.json", "r") as f:
            content = f.read().strip()
            if not content:
                return None
            return json.loads(content)
    except FileNotFoundError:
        return None