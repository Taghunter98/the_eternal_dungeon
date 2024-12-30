# Import the character module
import character
import mechanics
import levels
import story

class MainGame:
    def __init__(self):
        # Start the game
        self.start_game()

    def start_game(self):
        print("\nChecking for save...")
        mechanics.sleep(1)

        # Call check_save() once and reuse the result
        save = MainGame.check_save()  

        if save == "":
            # Start a new game
            print("No save file found. Starting a new adventure!")
            character.character_creator() 
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
            print(f"Welcome back, adventurer {player.    character_name}!")
            print(f"You are currently on {save}.")
            mechanics.sleep(1)

            # Main game loop
            self.game_loop(player, inventory, save)

    def game_loop(self, player, inventory, save):
        while True:
            mechanics.sleep(2)
            mechanics.print_spacing()
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
    }
    
    def continue_story(player, inventory, save):
        levels = MainGame.level_map
        if save in levels:
            levels[save](player, inventory)
        else:
            mechanics.error("No progress found.")
            mechanics.sleep(1)

# Start the game
if __name__ == "__main__":
    MainGame()
