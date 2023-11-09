from player import Player
from display_dice import display_dice
from scoring import Scoring

class PlayYahtzee(Player):
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.players = [Player() for _ in range(num_players)]
        self.current_player_index = 0
        

    def next_player(self):
        """Switch to the next player for their turn."""
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def roll(self, player):
        """Initiates a dice roll and displays the results."""
        print("\nRolling the dice...")
        player.turn.roll()
        display_dice(player.turn.get_state()['dice_values'])

    def choose_category(self, player):
        """Allows the player to choose a scoring category."""
        print("\nChoosing a scoring category...")
        player.display_score_card()
        available_categories = player.remaining_categories()

        for category in available_categories:
            score = player.score.calculate_score(category, player.turn.get_state()['dice_values'])
            print(f"{category}: {score}")

        category_input = input("Enter the category to score: ")
        while category_input not in available_categories:
            print("Invalid category. Choose from the remaining categories.")
            category_input = input("Enter the category to score: ")

        score = player.score.calculate_score(category_input, player.turn.get_state()['dice_values'])
        player.score.mark_score(category_input, score)


    def start_new_turn(self, player):
        """Resets the game state for a new turn."""
        player.turn.rolls_left = 3
        player.held_dice = []

    def turn(self, player):
        """Manages a single turn in the game."""
        for roll_num in range(3):
            print(f"\nRoll {roll_num + 1}")
            self.roll(player)
            held_indices = player.turn.get_state()['held_dice']
            display_dice(player.turn.get_state()['dice_values'], held_indices)

            if roll_num < 2:  # Allow holding dice only for the first two rolls
                hold_input = input("Enter indices of dice to hold (space-separated, or 'none' to hold none): ")
                if hold_input.lower() != 'none':
                    indices_to_hold = [int(index) for index in hold_input.split()]
                    player.turn.hold(indices_to_hold)

            self.choose_category(player)

    def play_game(self):
        """The main game loop that calls other methods to progress the game."""
        rounds = 13  # Number of rounds in a Yahtzee game

        for _ in range(rounds):
            print(f"\nRound {_ + 1}")

            for player in self.players:
                print(f"\n{player.name}'s turn:")
                self.start_new_turn(player)
                self.turn(player)

        self.game_over()

    def generate_block_art(self):
        """Generates ASCII art for the game-over screen."""
        print("##########")
        print("# GAME OVER #")
        print("##########")

    def game_over(self):
        """Ends the game and displays the final score."""
        self.generate_block_art()
        print("\nFinal Scores:")
        for player in self.players:
            print(f"{player.name}: {sum(player.score.get_score_card().values())}")

# Run the game
if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    yahtzee_game = PlayYahtzee(num_players)
    yahtzee_game.play_game()
