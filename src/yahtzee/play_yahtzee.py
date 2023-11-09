from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self):
        self.player = Player()

    def roll(self):
        """
        Initiates a dice roll and displays the results.
        """
        self.player.turn.roll()  # Initiates a dice roll
        display_dice(self.player.turn.yahtzee_dice.get_values(), self.player.turn.held_dice)  # Displays the results

    def choose_category(self):
        """
        Allows the player to choose a scoring category.
        """
        self.player.turn.choose_category()

    def start_new_turn(self):
        """
        Resets the game state for a new turn.
        """
        self.player.turn = self.player.PlayerTurn(self.player)

    def turn(self):
        """
        Manages a single turn in the game.
        """
        while not self.player.turn.is_turn_over():
            self.roll()
            self.choose_category()

    def play_game(self):
        """
        The main game loop that calls other methods to progress the game.
        """
        print("Welcome to Yahtzee!")
        while not self.player.is_score_card_full():
            self.turn()
            self.start_new_turn()
        self.game_over()

    def game_over(self):
        """
        Displays the final score and ends the game.
        """
        print("Game Over!")
        display_dice(self.player.turn.yahtzee_dice.get_values(), self.player.turn.held_dice)
        self.player.display_score_card()
        print("Final Score:", self.player.get_total_score())
        self.generate_block_art()

    def generate_block_art(self):
        """
        Generates ASCII art for the game-over screen.
        """
        # Replace this with your own ASCII art or create a method to generate dynamic ASCII art
        block_art = """
        Game Over!
        ┌───────────────────┐
        │                   │
        │   Thanks for      │
        │   playing!        │
        │                   │
        └───────────────────┘
        """
        print(block_art)

# Example usage:
if __name__ == "__main__":
    yahtzee_game = PlayYahtzee()
    yahtzee_game.play_game()  # The main game loop
