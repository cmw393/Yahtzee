from player import Player

class PlayYahtzee:
    def __init__(self):
        self.player = Player()

    def roll(self):
        print("\nStarting a new turn")
        self.player.turn = self.player.PlayerTurn(self.player)
        print("Turn created successfully")
        print("Score card:", self.player.turn.scoring.get_score_card())
        rolled_values = self.player.turn.roll()
        print("Rolled values:", rolled_values)

    def choose_category(self):
        print("\nChoosing a category")
        valid_categories = self.player.turn.scoring.remaining_categories()
        print("Available Categories:", valid_categories)
        category = input("Choose a scoring category: ")

        if category not in valid_categories:
            print("Invalid category. Please choose a valid category.")
            self.choose_category()
        else:
            score = self.player.turn.scoring.calculate_score(category, self.player.turn.get_state()['dice_values'])
            self.player.turn.scoring.mark_score(category, score)
            print(f"Scored {score} points in {category}!")

    def start_new_turn(self):
        print("\nStarting a new turn")
        self.player.turn = self.player.PlayerTurn(self.player)
        print("Turn created successfully")

    def turn(self):
        print("\nTaking a turn")
        self.roll()
        self.hold_dice_prompt()
        self.roll()
        self.hold_dice_prompt()
        self.roll()
        self.choose_category()

    def play_game(self):
        print("\nPlaying the game")
        while not self.player.turn.scoring.is_full():
            self.start_new_turn()
            self.turn()
        self.game_over()

    def generate_block_art(self):
        print("Congratulations!")
        # Add your ASCII art here

    def game_over(self):
        print("\nGame Over!")
        self.player.display_score_card()
        self.generate_block_art()
        exit()

    def hold_dice_prompt(self):
        indices = input("Enter indices of dice to hold (e.g., 1 3 5), or press Enter to roll all dice: ")
        if indices:
            indices = [int(idx) - 1 for idx in indices.split()]
            self.player.turn.hold(indices)


if __name__ == "__main__":
    yahtzee_game = PlayYahtzee()
    yahtzee_game.play_game()
