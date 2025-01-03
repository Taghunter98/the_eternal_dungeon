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
        mechanics.print_spacing()
        dungeon_entrance(player, inventory)
    else:
        print("Quiting level...")
        mechanics.sleep(1)
        print(mechanics.return_to_menu)
        return 0
    
def level_two(player, inventory):
    mechanics.print_with_animation(story.level_2_intro)
    trap_room(player, inventory)

# Locked door
def dungeon_entrance(player, inventory):
    mechanics.print_with_animation(story.dungeon_door)
    print("Would you like to check your inventory for a key?")
    mechanics.dialog_simple("Yes", "No")
    
    choice = input(mechanics.response)
    
    if choice == "1":
        dungeon_key = character.player_inventory(player, inventory)  # Get the selected item
        if dungeon_key == "Dungeon Key":
            mechanics.sleep(1)
            mechanics.print_spacing()
            mechanics.print_with_animation(story.dungeon_door_success)
            mechanics.save_progress("first_battle")
            mechanics.sleep(1)
            mechanics.print_spacing()
            battle_one(player, inventory) # Continue story
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
def bridge_encounter(player, inventory):
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
    mechanics.sleep(1)
    mechanics.print_spacing()
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
    
# Level two trap room
def trap_room(player, inventory):
    print("You step into a dimly lit room filled with ancient, crumbling statues.")
    print("The air is thick with dust, and the faint sound of grinding mechanisms fills your ears.")
    mechanics.dialog_simple("Brave the traps", "Look for another way")

    choice = input(mechanics.response)
    if choice == "1":
        print("\nYou make a dash for the door, but a sudden *crack* echoes through the room!")
        print("The floor collapses beneath your feet, and you tumble into a dark chasm.")
        player.health -= 10
        mechanics.sleep(0.5)
        print("You take 10 damage!")
            
        print("\nAs you gather yourself, you hear something stirring in the shadows...")
        mechanics.dialog_simple("Challenge the creature!", "Try to sneak past")
            
        sub_choice = input(mechanics.response)
        if sub_choice == "1":
            print("\nYou steady yourself as a monstrous creature charges from the darkness!")
            mechanics.battle(player, inventory)
            print("After a fierce struggle, you emerge victorious and climb out of the chasm.")
            mechanics.save_progress("level_two_boss")
            return
        elif sub_choice == "2":
            print("\nYou press yourself against the wall and move cautiously past the beast.")
            print("The creature lets out a low growl but doesn't give chase.")
            print("You climb out of the chasm, shaken but unharmed.")
            mechanics.save_progress("level_two_boss")
            return
        else:
            mechanics.error("Invalid choice. The creature senses your hesitation and attacks!")
            mechanics.battle(player, inventory)
            print("You manage to fend off the creature and escape.")
            mechanics.save_progress("level_two_boss")
            return
            
    elif choice == "2":
        print("\nYou carefully examine the room and find a hidden passage behind a crumbling statue.")
        print("It leads you safely to the other side of the room, bypassing the traps.")
        mechanics.save_progress("level_two_boss")
        return
    else:
        mechanics.error("Invalid choice. Please choose a valid option.")
        
def level_two_boss(player, inventory):
    mechanics.print_spacing
    mechanics.print_with_animation(story.troll_boss_intro)
    mechanics.battle(player, inventory)
    mechanics.print_with_animation(story.troll_boss_victory)
    mechanics.save_progress("Level 3")
    return

def level_three(player, inventory):
    mechanics.print_spacing
    mechanics.print_with_animation(story.level_3_intro)
    bridge_encounter(player, inventory)
    

def second_battle(player, inventory):
    mechanics.print_with_animation(story.ancient_tomb_ambush)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.battle(player, inventory)
    mechanics.print_with_animation(story.ancient_tomb_victory)
    mechanics.save_game("final_boss")

def final_boss(player, inventory):
    print("WORK IN PROGRESS")
    return