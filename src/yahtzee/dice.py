import random
from dataclasses import dataclass
from typing import List
from dataclasses import dataclass, field, post_init
@dataclass
class Dice:
    sides: int = 6
    current_value: int = None
    def roll(self) -> int:
        """Roll the dice and update the current value."""
        self.current_value = random.randint(1, self.sides)
        return self.current_value

@dataclass
class YahtzeeDice(Dice):
    num_dice: int = 5
    dice_set: list[Dice] = field(default_factory=list)
    @post_init
    def _initialize_dice_set(self):
        """Initialize the dice_set attribute with a list of Dice objects."""
        self.dice_set = [Dice() for _ in range(self.num_dice)]

    def roll(self, keep: list[bool] = None) -> list[int]:
        """
        Roll the Yahtzee dice, updating the current values.
        If keep is provided, keep the values of the corresponding dice.
        """
        rolled_values = []
        for i in range(self.num_dice):
            if keep and keep[i]:
                rolled_values.append(self.dice_set[i].current_value)
            else:
                rolled_values.append(self.dice_set[i].roll())
        return rolled_values

    def roll_all(self) -> list[int]:
        """Roll all the dice in dice_set and return a list of the rolled values."""
        return [dice.roll() for dice in self.dice_set]

    def get_values(self) -> list[int]:
        """Return a list containing the current values of all dice in dice_set."""
        return [dice.current_value for dice in self.dice_set]