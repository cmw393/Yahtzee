import pytest
from yahtzee.dice import Dice,YahtzeeDice

@pytest.fixture
def yahtzee_dice():
    return YahtzeeDice()

def test_roll_all(yahtzee_dice):
    values_before_roll = yahtzee_dice.get_values()
    yahtzee_dice.roll_all()
    values_after_roll = yahtzee_dice.get_values()

    assert values_before_roll != values_after_roll

def test_roll_with_keep(yahtzee_dice):
    yahtzee_dice.roll_all()
    values_before_roll = yahtzee_dice.get_values()

    # Keep the first two dice values
    keep = [True, True, False, False, False]
    yahtzee_dice.roll(keep)
    values_after_roll = yahtzee_dice.get_values()

    assert values_before_roll[:2] == values_after_roll[:2]
    assert values_before_roll[2:] != values_after_roll[2:]

def test_roll_without_keep(yahtzee_dice):
    values_before_roll = yahtzee_dice.get_values()
    yahtzee_dice.roll()
    values_after_roll = yahtzee_dice.get_values()

    assert values_before_roll != values_after_roll

def test_initialization_of_dice_set(yahtzee_dice):
    assert len(yahtzee_dice.dice_set) == yahtzee_dice.num_dice
    assert all(isinstance(dice, Dice) for dice in yahtzee_dice.dice_set)


