from unittest.mock import patch
from yahtzee.display_dice import display_dice
from typing import List
from io import StringIO

def test_display_dice(capsys):
    values = [1, 2, 3, 4, 5]
    held_indices = [1, 3]

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        display_dice(values, held_indices)
        captured_output = mock_stdout.getvalue()

    expected_output = (
        "  _______    _______    _______    _______    _______  \n"
        " |       |  | •     |  | •     |  | •   • |  | •   • | \n"
        " |   •   |  |       |  |   •   |  |       |  |   •   | \n"
        " |       |  |     • |  |     • |  | •   • |  | •   • | \n"
        "  -------    -------    -------    -------    -------  \n"
    )

    assert captured_output == expected_output

def test_display_dice_no_held(capsys):
    values = [6, 5, 4, 3, 2]

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        display_dice(values)
        captured_output = mock_stdout.getvalue()

    expected_output = (
        "  _______    _______    _______    _______    _______  \n"
        " | •   • |  | •   • |  | •   • |  | •   • |  | •   • | \n"
        " | •   • |  | •   • |  | •   • |  | •   • |  | •   • | \n"
        " | •   • |  | •   • |  | •   • |  | •   • |  | •   • | \n"
        "  -------    -------    -------    -------    -------  \n"
    )

    assert captured_output == expected_output
