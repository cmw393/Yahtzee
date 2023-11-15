import pytest
from yahtzee.display_dice import display_dice


def test_display_dice(capsys):
    # Test displaying dice with no held indices
    values = [1, 2, 3, 4, 5]
    display_dice(values)
    captured = capsys.readouterr()
    assert "  _______  \n |       | \n |   •   | \n |_______| \n" in captured.out
    assert "  _______  \n | •     | \n |       | \n |____•__| \n" in captured.out
    assert "  _______  \n | •     | \n |   •   | \n |____•__| \n" in captured.out
    assert "  _______  \n | •   • | \n |       | \n | •___• | \n" in captured.out
    assert "  _______  \n | •   • | \n |   •   | \n | •___• | \n" in captured.out
    assert "  _______  \n | •   • | \n | •   • | \n | •___• | \n" in captured.out

    # Test displaying dice with some held indices
    values = [1, 2, 3, 4, 5]
    held_indices = [0, 2, 4]
    display_dice(values, held_indices)
    captured = capsys.readouterr()
    assert "\033[92m  _______  \n |       | \n |   •   | \n |_______| \n\033[92m" in captured.out
    assert "  _______  \n | •     | \n |       | \n |____•__| \n" in captured.out
    assert "\033[92m  _______  \n | •     | \n |   •   | \n |____•__| \n\033[92m" in captured.out
    assert "  _______  \n | •   • | \n |       | \n | •___• | \n" in captured.out
    assert "\033[92m  _______  \n | •   • | \n |   •   | \n | •___• | \n\033[92m" in captured.out
    assert "  _______  \n | •   • | \n | •   • | \n | •___• | \n" in captured.out