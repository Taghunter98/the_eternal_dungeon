# Import the character module
import character
import mechanics
import levels
import story

class MainGame:
    def __init__(self):
        # Initialize the game
        self.start_game()

    def start_game(self):
        # Load save if found
        if MainGame.check_save() == 1:
            MainGame.create_character()
        else:
            print("Save found")
            player = mechanics.load_character()
            inventory = mechanics.load_inventory()
            save = MainGame.check_save()
            print("Save loaded successfully!")
            print(story.title_card)
            print(f"Welcome back adventurer {player.character_name}!")
            print(f"You are currently on {save}.")
            # Main game loop
            self.game_loop(player, inventory, save)

    def game_loop(self, player, inventory, save):
        while True:
            # Example game loop to handle player actions
            mechanics.dialog_advanced("View Inventory", "View Character Sheet", "Continue Quest", "Exit Game")

            choice = input(mechanics.response)

            if choice == "1":
                character.display_inventory(player, inventory)
            elif choice == "2":
                character.display_character_sheet(player, inventory)
            elif choice == "3":
                MainGame.continue_story(player, save)
            elif choice == "4":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    # Character creation function
    def create_character():
    # Create a player character
        player = character.character_creator()
        mechanics.save_character(player)
        mechanics.save_inventory(character.inventory)
        mechanics.save_progress("Level 1")
        return player

    # Function to check for save
    def check_save():
        save = mechanics.load_progress()
        if save:
            return save
        elif save == 1:
            return save
        else:
            print("No valid save file found.")
            return 1  # Default to new game
    
    # Function to continue story
    def continue_story(player, save):
        if save == "Level 1":
            levels.level_one(player)
        else:
            mechanics.error("No progress found.")

# Start the game
if __name__ == "__main__":
    MainGame()
