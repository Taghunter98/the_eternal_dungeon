# Import the character module
import character
import mechanics
import levels
import story
import sys

class MainGame:
    def __init__(self):
        # Start the game
        self.start_game()

    def start_game(self):
        print("\nChecking for save...")
        mechanics.sleep(1)

        # Call check_save() once and reuse the result
        save = MainGame.check_save()  

        if save == "Level 1":
            player = character.character_creator()
            inventory = character.inventory
            mechanics.save_game(player, inventory)
            
            # Start main game loop
            self.game_loop(player, inventory, save) 
            
        else:
            # Load existing progress
            print("Save found!")
            mechanics.sleep(1)
            player = mechanics.load_character()  
            inventory = mechanics.load_inventory()
            print("Save loaded successfully!")
            mechanics.sleep(1)
            
            # Resume game with stats
            mechanics.print_with_animation(story.title_card)
            print(f"Welcome back, adventurer {player.character_name}!")
            print(f"You are currently on {save}.")
            mechanics.sleep(1)

            # Main game loop
            self.game_loop(player, inventory, save)

    def game_loop(self, player, inventory, save):
        while True:
            mechanics.sleep(2)
            mechanics.print_spacing()
            # Get save
            save = mechanics.load_progress()
            # Example game loop to handle player actions
            mechanics.dialog_advanced("View Inventory", "View Character Sheet", "Continue Quest", "Exit Game")

            choice = input(mechanics.response)

            if choice == "1":
                mechanics.print_spacing()
                character.player_inventory(player, inventory)
            elif choice == "2":
                mechanics.print_spacing()
                character.display_character_sheet(player, inventory)
            elif choice == "3":
                mechanics.print_spacing()
                MainGame.continue_story(player, inventory, save)
            elif choice == "4":
                print("Thanks for playing!")
                mechanics.sleep(0.5)
                print("Quitting game...")
                mechanics.sleep(1)
                break
            else:
                print("Invalid choice. Please try again.")
    
    # Character creation function
    def create_character():
        player = character.character_creator()
        mechanics.save_character(player)
        mechanics.save_inventory(character.inventory)
        mechanics.save_progress("Level 1")
        return player

    # Function to check for save
    def check_save():
        progress = mechanics.load_progress()  # Load progress once.
        if progress:
            return progress
        else:
            print("No valid save file found. Starting a new game...")
            return "Level 1"  # Default starting point for a new game.

    
    # Function to continue story
    level_map = {
        "Level 1": levels.level_one,
        "dungeon_entrance": levels.dungeon_entrance,
        "first_battle": levels.battle_one,
        "Level 2": levels.level_two,
        "level_two_boss": levels.level_two_boss,
        "Level 3": levels.level_three,
        "final_boss": levels.final_boss
    }
    
    def continue_story(player, inventory, save):
        levels = MainGame.level_map
        if save in levels:
            levels[save](player, inventory)
        else:
            mechanics.error("No progress found.")
            mechanics.sleep(1)
    
    def game_over():
        print("Game Over!")
        mechanics.sleep(0.5)
        print("Quitting game...")
        mechanics.sleep(1)
        sys.exit()

# Start the game
if __name__ == "__main__":
    MainGame()
