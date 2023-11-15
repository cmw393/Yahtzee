from yahtzee.dice_display import display_dice
import pytest
from io import StringIO
import sys


def test_display_dice(capsys):
    values = [1, 2, 3, 4, 5, 6]
    held_indices = [1, 3, 5]

    expected_output = """  _______  
 |       | 
 |   •   | 
 |_______| 
[0m
  _______  
 | •     | 
 |       | 
 |____•__| 
[92m  _______  
 | •   • | 
 |       | 
 | •___• | 
[0m
  _______  
 | •   • | 
 |   •   | 
 | •___• | 
[92m  _______  
 | •   • | 
 | •   • | 
 | •___• | 
[0m
"""

    display_dice(values, held_indices)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_display_dice_no_held(capsys):
    values = [1, 2, 3, 4, 5, 6]
    expected_output = """  _______  
 |       | 
 |   •   | 
 |_______| 
[0m
  _______  
 | •     | 
 |       | 
 |____•__| 
[0m
  _______  
 | •     | 
 |   •   | 
 |____•__| 
[0m
  _______  
 | •   • | 
 |       | 
 | •___• | 
[0m
  _______  
 | •   • | 
 |   •   | 
 | •___• | 
[0m
  _______  
 | •   • | 
 | •   • | 
 | •___• | 
[0m
"""

    display_dice(values)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_display_dice_invalid_values(capsys):
    values = [7, 8, 9]
    with pytest.raises(KeyError, match="Invalid dice value"):
        display_dice(values)


def test_display_dice_invalid_held_indices(capsys):
    values = [1, 2, 3, 4, 5, 6]
    held_indices = [6, 7, 8]
    with pytest.raises(IndexError, match="Invalid index in held_indices"):
        display_dice(values, held_indices)


if __name__ == "__main__":
    pytest.main()
