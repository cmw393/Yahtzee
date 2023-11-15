import pytest
from yahtzee.scoring import Scoring

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
