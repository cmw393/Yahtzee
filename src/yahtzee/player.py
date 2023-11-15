from typing import List
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self, name):
        super().__init__()  # Initialize the Scoring base class
        self.name = name
        self.score = 0
        self.turn = self.PlayerTurn(self)

# Inside the Player class
    class PlayerTurn:
        def __init__(self, player_instance):
            self.yahtzee_dice = YahtzeeDice()  # Assuming you have a YahtzeeDice class
            self.rolls_left = 3
            self.held_dice = []
            self.player_instance = player_instance
            self.scoring = Scoring()
            self.dice_to_roll = []
        def roll(self):
            """
            Rolls all dice not being held, updates their values, and decrements rolls_left.
            """
            if self.rolls_left > 0:
                # Determine indices of dice not being held
                self.dice_to_roll = [i in self.held_dice for i in range(self.yahtzee_dice.num_dice)]

                # Roll the remaining dice
                rolled_values = self.yahtzee_dice.roll(keep=self.dice_to_roll)

                # Update held_dice and rolls_left
                self.held_dice = []
                self.rolls_left -= 1

                return rolled_values
            else:
                print("No more rolls left in this turn.")
                return [] 

        def hold(self, indices: List[int]):
            """
            Accepts a list of indices and updates held_dice to hold those dice.
            """
            self.held_dice = indices
        def get_state(self):
            """
            Returns a dictionary containing the current state of the turn (dice_values, rolls_left, held_dice).
            """
            return {
                'dice_values': self.yahtzee_dice.get_values(),
                'rolls_left': self.rolls_left,
                'held_dice': self.held_dice
            }