from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self):
        super().__init__()  # Initialize the Scoring base class
        self.name = input("Enter your name: ")
        self.score = 0
    
        class PlayerTurn:
                def __init__(self, player_instance):
                    self.yahtzee_dice = YahtzeeDice()  # Assuming you have a YahtzeeDice class
                    self.rolls_left = 3
                    self.held_dice = []
                    self.player_instance = player_instance
                
                def roll(self):
                    """
                    Rolls all dice not being held, updates their values, and decrements rolls_left.
                    """
                    if self.rolls_left > 0:
                        # Determine indices of dice not being held
                        dice_to_roll = [i for i in range(self.yahtzee_dice.num_dice) if i not in self.held_dice]

                        # Roll the remaining dice
                        rolled_values = self.yahtzee_dice.roll(keep=[False] * self.yahtzee_dice.num_dice)

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
                

        # Create an instance of the nested PlayerTurn class
        self.turn = self.PlayerTurn(self)