import mechanics
import story
import the_eternal_dungeon
import random

def level_one(player):
    print(story.level_1_intro)
    mechanics.dialog_simple("Begin level 1", "Back to menu")
    choice = input(mechanics.response)
    if choice == "1":
        bridge_encounter(player)
    else:
        print("Quiting level...")
        return 0

# Bridge encounter where player has to cross a bridge
def bridge_encounter(player):
    print(story.bridge_encounter)
    mechanics.dialog_simple("Cross the bridge", "Try and swim")
    choice = input(mechanics.response)
    if choice == "1":
        print("\nYou cautiously step onto the bridge, each footfall echoing ominously. Halfway across, you hear a loud *crack*...")
        # Simulate a random event
        if random.randint(1, 10) > 3:  # 70% chance of success
            print("The bridge holds! You breathe a sigh of relief and continue to the other side.")
        else:
            print("The bridge gives way! You fall into the icy water below, battered by the current. You manage to swim to the shore but lose some health.")
            player.health -= 10
    elif choice == "2":
        print("\nYou plunge into the freezing water, the cold stealing your breath. The current is strong, but you fight against it...")\
        # Simulate a random event
        if random.randint(1, 10) > 4:  # 60% chance of success
            print("You manage to swim across and pull yourself onto the far shore, drenched and shivering but alive.")
        else:
            print("The current overwhelms you! You barely manage to crawl onto the shore, exhausted and injured.")
            player.health -= 15
    else:
        print("\nIndecision is dangerous here. You must choose a path!")
        bridge_encounter(player)  # Restart the encounter