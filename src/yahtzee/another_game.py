import random

class YahtzeeGame:
    def __init__(self):
        self.dice_values = [0, 0, 0, 0, 0]
        self.rolls_left = 3

    def roll_dice(self, keep=None):
        if keep is None:
            self.dice_values = [random.randint(1, 6) for _ in range(5)]
        else:
            for i in range(5):
                if not keep[i]:
                    self.dice_values[i] = random.randint(1, 6)

    def display_dice(self):
        print("Current Dice Values:", self.dice_values)

    def play_turn(self):
        print(f"\nStarting a new turn. Rolls left: {self.rolls_left}")

        # Create a new set of dice for the turn
        self.roll_dice()

        while self.rolls_left > 0:
            self.display_dice()
            if self.rolls_left > 1:
                keep = self.choose_dice_to_keep()
                self.roll_dice(keep)
                self.display_dice()

            self.rolls_left -= 1

    def choose_dice_to_keep(self):
        keep = [False] * 5
        indices = input("Enter indices of dice to keep (e.g., 1 3 5), or press Enter to keep none: ")
        if indices:
            indices = [int(idx) - 1 for idx in indices.split()]
            for idx in indices:
                keep[idx] = True
        return keep

if __name__ == "__main__":
    yahtzee_game = YahtzeeGame()
    yahtzee_game.play_turn()
