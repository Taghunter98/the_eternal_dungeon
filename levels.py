import mechanics
import character
import story
import enemy

import random

def level_one(player, inventory):
    mechanics.print_with_animation(story.level_1_intro)
    mechanics.dialog_simple("Begin level 1", "Back to menu")
    choice = input(mechanics.response)
    
    if choice == "1":
        mechanics.save_progress("dungeon_entrance")
        dungeon_entrance(player, inventory)
    else:
        print("Quiting level...")
        mechanics.sleep(1)
        print(mechanics.return_to_menu)
        return 0

# Locked door
def dungeon_entrance(player, inventory):
    mechanics.print_with_animation(story.dungeon_door)
    print("Would you like to check your inventory for a key?")
    mechanics.dialog_simple("Yes", "No")
    
    choice = input(mechanics.response)
    
    if choice == "1":
        dungeon_key = character.player_inventory(player, inventory)  # Get the selected item
        if dungeon_key == "Dungeon Key":
            mechanics.print_with_animation(story.dungeon_door_success)
            mechanics.save_progress("first_battle")
            first_battle(player, inventory) # Continue story
            return
        else:
            mechanics.print_with_animation(story.dungeon_door_failure)
            return
    elif choice == "2":
        print("You decide to look around the area for another way...")
        # Optional: Add exploration logic here
    else:
        mechanics.error("Invalid response.")
        return
    
    
# Bridge encounter where player has to cross a bridge
def bridge_encounter(player):
    print(story.bridge_encounter)
    mechanics.dialog_simple("Cross the bridge", "Try and swim")
    choice = input(mechanics.response)
    if choice == "1":
        print("\nYou cautiously step onto the bridge, each footfall echoing ominously. Halfway across, you hear a loud *crack*...")
        
        # Roll die
        die = mechanics.roll_die()
        
        if die > 3:
            print("The bridge holds! You breathe a sigh of relief and continue to the other side.")
        else:
            print("The bridge gives way! You fall into the icy water below, battered by the current. You manage to swim to the shore but lose some health.")
            player.health -= 10
    elif choice == "2":
        print("\nYou plunge into the freezing water, the cold stealing your breath. The current is strong, but you fight against it...")\
        
        # Roll die
        die = mechanics.roll_die()
        
        if die > 5:
            print("You manage to swim across and pull yourself onto the far shore, drenched and shivering but alive.")
        else:
            print("The current overwhelms you! You barely manage to crawl onto the shore, exhausted and injured.")
            player.health -= 15
    else:
        print("\nIndecision is dangerous here. You must choose a path!")
        bridge_encounter(player)  # Restart the encounter
        

# Level 1 Battle
def battle_one(player, inventory):
    mechanics.print_with_animation(story.first_battle)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.print_with_animation(story.battle_victory)
    
    # Post battle chest reward
    mechanics.dialog_simple("Next Level", "You look around and notice a chest nearby. What will you do?")
    choice = input(mechanics.response)

    if choice == "1":
        print("\nYou decide to leave the chest behind and venture deeper into the Eternal Dungeon...")
        mechanics.save_progress("Level 2")
        return
    elif choice == "2":
        print("\nYou approach the chest and notice it is locked. Perhaps you can break it open?")
        break_chance = mechanics.dice()

        exit_text = "\nWith no other options, you leave the room and continue deeper into the dungeon..."
        
        if break_chance > 4:
            print("\nWith a mighty strike, you shatter the lock and open the chest!")
            print("Inside, you find 50 Gold!")
            inventory["Gold"] += 50  # Properly updates the inventory
            print(exit_text)
            mechanics.save_progress("Level 2")
            mechanics.sleep(2)
            return
        else:
            print("\nYou strike the lock with all your strength, but it refuses to budge...")
            print(exit_text)
            mechanics.save_progress("Level 2")
            mechanics.sleep(2)
            return
    else:
        print("\nIndecision grips you. Time waits for no one, and you press onward...")
        mechanics.save_progress("Level 2")
        return