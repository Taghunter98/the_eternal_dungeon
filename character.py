import mechanics

# TODO
# Add dexterity
# Add Strength
# Add Inteligence
# Add abilities
# Battle logic

def character_creator():
    player_name = character.create_name()
    player_class = character.class_type()
    player = character(player_name, player_class)
    print(f"Welcome adventurer {player.character_name}.\nYou are a {player.character_class}")
    if player_class == "Warrior":
        warrior_class(player)
    elif player_class == "Mage":
        mage_class(player)
    elif player_class == "Rogue":
        rogue_class(player)
    elif player_class == "Cleric":
        cleric_class(player)

    return player

class character:
    def __init__(self, character_name, character_class):
        self.character_name = character_name
        self.character_class = character_class
        self.health = 0
        self.stamina = 0
        self.magic = 0
        self.abilities = []
    
    # creates name for character
    def create_name():
        print("Greetings, traveler. You have journeyed far to reach these lands...")
        print("Tell me, what name shall echo in the annals of history?")
        name = input(mechanics.response)
        print(f"Ah, {name}... a name destined for greatness, or perhaps folly.")
        return name

    # creates class type based on int input
    def class_type():
        print("\nNow, to survive the perils that await, you must choose your path.")
        print("This realm is fraught with danger, and each choice will shape your destiny.")
        print("Do you wish to see the available classes, or have you already decided?")
    
        mechanics.dialog_simple("Show me the classes", "I know my path")
        option = input(mechanics.response)
    
        if option == "1":
            print("\nAllow me to introduce the paths you may follow:")
            print("- [1] Warrior: A fearless fighter with unmatched strength and resilience.")
            print("- [2] Mage: A master of arcane arts, wielding spells of devastating power.")
            print("- [3] Rogue: A cunning shadow, striking swiftly and silently.")
            print("- [4] Cleric: A holy protector, calling upon divine powers to heal and smite.")
            print("\nChoose wisely, for your decision is final.")
            player_class = int(input(mechanics.response))
            return character.class_options(player_class)
    
        elif option == "2":
            print("\nAh, a seasoned adventurer, are we? Then speak your choice:")
            mechanics.dialog_advanced("Warrior", "Mage", "Rogue", "Cleric")
            player_class = int(input(mechanics.response))
            return character.class_options(player_class)
    
        else:
            mechanics.error("I do not understand. Choose wisely.")
            return class_type()

    
    # helper method for class options
    def class_options(option):
        if option == 1:
            return "Warrior"
        elif option == 2:
            return "Mage"
        elif option == 3:
            return "Rogue"
        elif option == 4:
            return "Cleric"
        else:
            mechanics.error("Incorrect choice option")
            class_type()

def warrior_class(player):
    player.health = 100
    player.stamina = 30
    player.magic = 10
    player.abilities = ["Shield Bash", "Battle Cry"]
    
    # Update inventory
    inventory["Gold"] += 10
    inventory["Weapons"].append("Greatsword")
    inventory["Armour"].extend(["Chestplate", "Helmet", "Gauntlets", "Greaves"])
    inventory["Potions"].append({"Healing": 2})
    inventory["Quest Items"].extend(["Dungeon Key", "Warrior's Talisman"])

def mage_class(player):
    player.health = 30
    player.stamina = 20
    player.magic = 100
    player.abilities = ["Fireball", "Arcane Barrier"]
    
    # Update inventory
    inventory["Gold"] += 10
    inventory["Weapons"].extend(["Staff", "Dagger"])
    inventory["Armour"].extend(["Mage Hat", "Mage Robes", "Mage Gloves", "Mage Boots"])
    inventory["Potions"].extend([{"Healing": 2}, {"Magic": 2}])
    inventory["Quest Items"].extend(["Dungeon Key", "Mages's Talisman"])

def rogue_class(player):
    player.health = 60
    player.stamina = 100
    player.magic = 20
    player.abilities = ["Backstab", "Vanish"]
    
    # Update inventory
    inventory["Gold"] += 10
    inventory["Weapons"].extend(["Dagger"])
    inventory["Armour"].extend(["Hood", "Leather Jerkin", "Gloves", "Boots"])
    inventory["Potions"].extend([{"Healing": 2}, {"Stamina": 2}])
    inventory["Quest Items"].extend(["Dungeon Key", "Rogue's Talisman"])

def cleric_class(player):
    player.health = 70
    player.stamina = 50
    player.magic = 80
    player.abilities = ["Heal", "Divine Smite"]
    
    # Update inventory
    inventory["Gold"] += 10
    inventory["Weapons"].extend(["Staff", "Sword"])
    inventory["Armour"].extend(["Holy Hood", "Holy Armour", "Gauntlets", "Greaves"])
    inventory["Potions"].extend([{"Healing": 2}, {"Magic": 2}])
    inventory["Quest Items"].extend(["Dungeon Key", "Mages's Talisman"])


# Inventory

inventory = {
    "Gold": 0,
    "Weapons": [],
    "Armour": [],
    "Potions": [],
    "Quest Items": []
}

def display_inventory(player, inventory):
    print("+-------------------------------------------------+")
    print("|                   INVENTORY                     |")
    print("+-------------------------------------------------+")
    print(f" Gold: {inventory['Gold']:<41}")
    print("+----------------+----------------+---------------+")
    print("| Weapons        | Armour         | Potions       |")
    print("+----------------+----------------+---------------+")

    # Display items
    max_rows = max(len(inventory["Weapons"]), len(inventory["Armour"]), len(inventory["Potions"]))
    for i in range(max_rows):
        
        weapons = inventory["Weapons"][i] if i < len(inventory["Weapons"]) else ""
        armour = inventory["Armour"][i] if i < len(inventory["Armour"]) else ""

        # Potions with sublists or dictionaries
        if i < len(inventory["Potions"]):
            if isinstance(inventory["Potions"][i], dict):
                # Convert dictionary to a readable string (e.g., "Healing x2")
                potion_type, count = next(iter(inventory["Potions"][i].items()))
                potions = f"{potion_type} x{count}"
            else:
                potions = inventory["Potions"][i]
        else:
            potions = ""

        # Print each row
        print(f"| {weapons:<14} | {armour:<14} | {potions:<13} |")

    print("+----------------+----------------+---------------+")
    print("| Quest Items                                     |")
    print("+-------------------------------------------------+")
    print(f"{', '.join(inventory['Quest Items'])[:45]:<45}  ")
    print("+-------------------------------------------------+")

def player_inventory(player, inventory):
    # Prints out UI for inventory
    display_inventory(player, inventory)
    print("[1] Use Item   [2] Drop Item   [3] Back to Menu\n")
    
    choice = input(mechanics.response)

    if choice == "1":  # Choosing to use an item
        mechanics.dialog_simple("Use a potion", "Use a Quest Item")
        choice = input(mechanics.response)
        
        if choice == "1" and inventory["Potions"]:  # Check if potions are available
            mechanics.dialog_advanced("Use a Healing Potion", "Use a Magic Potion", "Use a Stamina Potion", "Back to Menu")
            potion_choice = input(mechanics.response)
            
            # Use Healing Potion
            if potion_choice == "1":
                for potion in inventory["Potions"]:
                    if isinstance(potion, dict) and "Healing" in potion:
                        if potion["Healing"] > 0:
                            player.health += 20
                            potion["Healing"] -= 1
                            print("You used a Healing Potion. Health restored by 20.")
                            mechanics.save_game(player, inventory)
                            break
                        else:
                            print("No Healing Potions left!")
                            break

            # Use Magic Potion
            elif potion_choice == "2":
                for potion in inventory["Potions"]:
                    if isinstance(potion, dict) and "Magic" in potion:
                        if potion["Magic"] > 0:
                            player.magic += 15
                            potion["Magic"] -= 1
                            print("You used a Magic Potion. Magic restored by 15.")
                            mechanics.save_game(player, inventory)
                            mechanics.sleep(1)
                            print(mechanics.return_to_menu)
                            break
                        else:
                            print("No Magic Potions left!")
                            mechanics.sleep(1)
                            print(mechanics.return_to_menu)
                            break

            # Use Stamina Potion
            elif potion_choice == "3":
                for potion in inventory["Potions"]:
                    if isinstance(potion, dict) and "Stamina" in potion:
                        if potion["Stamina"] > 0:
                            player.stamina += 10
                            potion["Stamina"] -= 1
                            print("You used a Stamina Potion. Stamina restored by 10.")
                            mechanics.save_game(player, inventory)
                            mechanics.sleep(1)
                            print(mechanics.return_to_menu)
                            break
                        else:
                            print("No Stamina Potions left!")
                            mechanics.sleep(1)
                            print(mechanics.return_to_menu)
                            break

            # Back to menu
            elif potion_choice == "4":
                print(mechanics.return_to_menu)
                return
            
            else:
                print("Invalid choice. ", mechanics.return_to_menu)
                
        elif choice == "2":
            print("\nWhich item do you want to use?")
    
            # Display items with proper indexing
            for index, item in enumerate(inventory["Quest Items"], start=1):
                print(f"[{index}] {item}")
    
            # Add option to go back to the menu
            print(f"[{len(inventory['Quest Items']) + 1}] Back to Menu")

            # Get player choice
            choice = input(mechanics.response)
    
            if choice.isdigit():  # Ensure the input is numeric
                choice = int(choice)
                if 1 <= choice <= len(inventory["Quest Items"]):
                    # Use the chosen quest item
                    selected_item = inventory["Quest Items"][choice - 1]
                    print(f"You used {selected_item}.")
                    return selected_item
                    # Remove the item after use
                    # inventory["Quest Items"].remove(selected_item)
                elif choice == len(inventory["Quest Items"]) + 1:
                    mechanics.sleep(1)
                    print(mechanics.return_to_menu)
                    return
                else:
                    mechanics.error("Invalid response.")
                    mechanics.sleep(1)
                    print(mechanics.return_to_menu)
                    return
        else:
            mechanics.error("Invalid response. Please enter a number.")
            mechanics.sleep(1)
            print(mechanics.return_to_menu)
            return
    elif choice == "2":
        print("Feature not yet implemented.")
        mechanics.sleep(1)
        print(mechanics.return_to_menu)
        return
    else:
        print("Invalid choice.")
        mechanics.sleep(1)
        print(mechanics.return_to_menu)
        return
                        
                        
                        

# Character sheet

def display_character_sheet(player, inventory):
    print("+-------------------------------------------------+")
    print("|                  CHARACTER SHEET                |")
    print("+-------------------------------------------------+")
    print(f" Name: {player.character_name:<41}")
    print(f" Class: {player.character_class:<40}")
    print("+----------------+----------------+---------------+")
    print(f" Health: {player.health:<7}   Stamina: {player.stamina:<7}   Magic: {player.magic:<7}")
    print("+----------------+----------------+---------------+")
    print(f" Abilities:")
    print("+-------------------------------------------------+")
    for ability in player.abilities:
        print(f"- {ability}")
    print("+-------------------------------------------------+")
    print("[1] Level Up   [2] Back to Menu\n                  ")
    character_sheet_options(player, inventory)

def character_sheet_options(player, inventory):
    
    choice = input(mechanics.response)
    gold_required = check_current_level() # Get gold level
    
    if choice == "1" and inventory["Gold"] >= gold_required:
        # Print message
        mechanics.dialog_advanced(f"Level Health [{gold_required} gold]", f"Level Stamina [{gold_required} gold]", f"Level Magic [{gold_required} gold]", "Back to Menu")
        
        choice = input(mechanics.response)
        
        if choice == "1":  # Level up Health
            player.health += 10
            inventory["Gold"] -= gold_required
            print(f"Your Health has increased to {player.health}!")
            mechanics.save_game(player, inventory)
            mechanics.sleep(1)
            print(mechanics.return_to_menu)
            
        elif choice == "2":  # Level up Stamina
            player.stamina += 10
            inventory["Gold"] -= gold_required
            print(f"Your Stamina has increased to {player.stamina}!")
            mechanics.save_game(player, inventory)
            mechanics.sleep(1)
            print(mechanics.return_to_menu)

        elif choice == "3":  # Level up Magic
            player.magic += 10
            inventory["Gold"] -= gold_required
            print(f"Your Magic has increased to {player.magic}!")
            mechanics.save_game(player, inventory)
            mechanics.sleep(1)
            print(mechanics.return_to_menu)

        elif choice == "4":  # Back to Menu
            mechanics.sleep(1)
            print(mechanics.return_to_menu)
            return
        else:
            print("Invalid choice!")
            mechanics.sleep(1)
            print(mechanics.return_to_menu)
    elif choice == "2":
        mechanics.sleep(1)
        print(mechanics.return_to_menu)

    else:
        print("Not enough gold to level up!")
        mechanics.sleep(1)
        print(mechanics.return_to_menu)
        return

def check_current_level():
    if mechanics.load_progress == "Level 1":
        return 20
    elif mechanics.load_progress == "Level 2":
        return 40
    elif mechanics.load_progress == "Level 3":
        return 60
    else:
        return 100 # default cost for higher levels for now

# Check character health
def check_health(player, inventory):
    if player.health <= 0:
        print("You died!")
        print("You will respawn at the last save point...")
        if player.class_type == "Warrior":
            warrior_class(player)
        elif player.class_type == "Mage":
            mage_class(player)
        elif player.class_type == "Rogue":
            rogue_class(player)
        elif player.player_class == "Cleric":
            cleric_class(player)
    
    # Save game
    print("Creating new save file...")
    mechanics.save_game(player, inventory)
    