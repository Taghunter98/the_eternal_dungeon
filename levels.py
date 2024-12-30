import mechanics
import character
import story

import random

def level_one(player, inventory):
    mechanics.print_with_animation(story.level_1_intro)
    mechanics.dialog_simple("Begin level 1", "Back to menu")
    choice = input(mechanics.response)
    
    if choice == "1":
        mechanics.save_progress("dungeon_entrance")
        mechanics.next_event()
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
            # Continue the story
            bridge_encounter(player)
        else:
            mechanics.print_with_animation(story.dungeon_door_failure)
    elif choice == "2":
        print("You decide to look around the area for another way...")
        # Optional: Add exploration logic here
    else:
        mechanics.error("Invalid response.")
    
    
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