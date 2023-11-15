from player import Player
from display_dice import display_dice
from play_yahtzee import PlayYahtzee

def test_yahtzee():
    # Create a player
    player = Player(name="TestPlayer")

    # Create a Yahtzee game
    yahtzee_game = PlayYahtzee(num_players=1)

    # Start a new turn for the player
    yahtzee_game.start_new_turn(player)

    # Display initial state
    display_state(player.turn)

    # Roll the dice for the first time
    player.turn.roll()
    display_state(player.turn)

    # Hold some dice
    held_indices = [0, 2, 4]
    player.turn.hold(held_indices)
    print(f"Held indices: {held_indices}")

    # Roll the dice again
    player.turn.roll()
    display_state(player.turn)

    # Continue testing as needed

def display_state(player_turn):
    state = player_turn.get_state()
    print(f"\nCurrent State:")
    print(f"Dice Values: {state['dice_values']}")
    print(f"Rolls Left: {state['rolls_left']}")
    print(f"Held Dice: {state['held_dice']}")

if __name__ == "__main__":
    test_yahtzee()
