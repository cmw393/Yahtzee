import pytest
from yahtzee.scoring import Scoring

def test_calculate_score():
    scoring = Scoring()
    assert scoring.calculate_score("Ones", [1, 2, 3, 4, 5]) == 1
    assert scoring.calculate_score("Twos", [1, 2, 3, 4, 5]) == 2
    assert scoring.calculate_score("Threes", [1, 2, 3, 4, 5]) == 3
    assert scoring.calculate_score("Fours", [1, 2, 3, 4, 5]) == 4
    assert scoring.calculate_score("Fives", [1, 2, 3, 4, 5]) == 5
    assert scoring.calculate_score("Sixes", [1, 2, 3, 4, 5]) == 0
    assert scoring.calculate_score("Three of a Kind", [1, 1, 1, 4, 5]) == 3
    assert scoring.calculate_score("Three of a Kind", [1, 1, 4, 4, 5]) == 0
    assert scoring.calculate_score("Four of a Kind", [1, 1, 1, 1, 5]) == 4
    assert scoring.calculate_score("Four of a Kind", [1, 1, 1, 5, 5]) == 0
    assert scoring.calculate_score("Full House", [1, 1, 2, 2, 2]) == 8
    assert scoring.calculate_score("Full House", [1, 1, 2, 2, 3]) == 0
    assert scoring.calculate_score("Small Straight", [1, 2, 3, 4, 6]) == 25
    assert scoring.calculate_score("Small Straight", [1, 2, 3, 4, 5]) == 0
    assert scoring.calculate_score("Large Straight", [1, 2, 3, 4, 5]) == 30
    assert scoring.calculate_score("Large Straight", [1, 2, 3, 4, 6]) == 0
    assert scoring.calculate_score("Yahtzee", [1, 1, 1, 1, 1]) == 50
    assert scoring.calculate_score("Yahtzee", [1, 1, 1, 1, 2]) == 0
    assert scoring.calculate_score("Chance", [1, 2, 3, 4, 5]) == 15

def test_mark_score():
    scoring = Scoring()
    scoring.mark_score("Ones", 3)
    assert scoring.get_score_card() == {"Ones": 3}
    with pytest.raises(ValueError):
        scoring.mark_score("Ones", 4)
    with pytest.raises(ValueError):
        scoring.mark_score("Invalid Category", 4)

def test_is_category_used():
    scoring = Scoring()
    scoring.mark_score("Ones", 3)
    assert scoring.is_category_used("Ones") == True
    assert scoring.is_category_used("Twos") == False

def test_remaining_categories():
    scoring = Scoring()
    scoring.mark_score("Ones", 3)
    assert sorted(scoring.remaining_categories()) == sorted(['Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three of a Kind', 'Four of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'])


def test_num_remaining_categories():
    scoring = Scoring()
    scoring.mark_score("Ones", 3)
    assert scoring.num_remaining_categories() == 12

def test_num_used_categories():
    scoring = Scoring()
    scoring.mark_score("Ones", 3)
    assert scoring.num_used_categories() == 1

def test_is_full():
    scoring = Scoring()
    assert scoring.is_full() == False
    for category in scoring.all_categories:
        scoring.mark_score(category, 0)
    assert scoring.is_full() == True