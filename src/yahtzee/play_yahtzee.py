from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self, num_players=1):
        self.players = [Player(name=input(f"Enter name for player {i + 1}: ")) for i in range(num_players)]

    def display_score_card(self, player):
        print("\nScore Card for", player.name)
        score_card = player.turn.scoring.get_score_card()
        for category, score in score_card.items():
            print(f"{category}: {score}")

    def start_new_turn(self, player):
        print(f"\nStarting a new turn for {player.name}")
        player.turn = player.PlayerTurn(player)
        print("Turn created successfully")

    def roll(self, player):
        print("\nStarting a new turn for", player.name)
        player.turn = player.PlayerTurn(player)
        print("Turn created successfully")

        # Call display_dice to show the dice art
        display_dice(player.turn.get_state()['dice_values'])

        print("Score card:", player.turn.scoring.get_score_card())
        rolled_values = player.turn.roll()
        self.display_rolled_dice(player, rolled_values)

    def choose_category(self, player):
        print(f"\nChoosing a category for {player.name}")
        valid_categories = player.turn.scoring.remaining_categories()
        print("Available Categories:", valid_categories)
        category = input("Choose a scoring category: ")

        if category not in valid_categories:
            print("Invalid category. Please choose a valid category.")
            self.choose_category(player)
        else:
            self.display_score_card(player)  # Display the scorecard
            score = player.turn.scoring.calculate_score(category, player.turn.get_state()['dice_values'])
            player.turn.scoring.mark_score(category, score)
            print(f"{player.name} scored {score} points in {category}!")

    def turn(self, player):
        print(f"\nTaking a turn for {player.name}")
        self.roll(player)
        self.hold_dice_prompt(player)
        self.roll(player)
        self.hold_dice_prompt(player)
        self.roll(player)
        self.choose_category(player)

    def play_game(self):
        print("\nPlaying the game")
        while not all(player.turn.scoring.is_full() for player in self.players):
            for player in self.players:
                self.start_new_turn(player)
                self.turn(player)
        self.game_over()

    def game_over(self):
        print("\nGame Over!")
        for player in self.players:
            player.display_score_card()
        self.generate_block_art()
        exit()

    def generate_block_art(self):
        print("Congratulations!")
        # Add your ASCII art here

    def hold_dice_prompt(self, player):
        indices = input(f"Enter indices of dice to hold for {player.name} (e.g., 1 3 5), or press Enter to roll all dice: ")
        if indices:
            indices = [int(idx) - 1 for idx in indices.split()]
            player.turn.hold(indices)

    def display_rolled_dice(self, player, rolled_values):
        print(f"{player.name}'s Rolled Dice:")
        display_dice(rolled_values)

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    yahtzee_game = PlayYahtzee(num_players)
    yahtzee_game.play_game()
