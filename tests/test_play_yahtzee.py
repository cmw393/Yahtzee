import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from yahtzee.play_yahtzee import PlayYahtzee

class TestPlayYahtzee(unittest.TestCase):

    @patch('builtins.input', side_effect=['Player1', ''])
    def test_init(self, mock_input):
        yahtzee_game = PlayYahtzee(num_players=1)
        self.assertEqual(len(yahtzee_game.players), 1)
        self.assertEqual(yahtzee_game.players[0].name, 'Player1')

    @patch('builtins.input', side_effect=['', '', 'Ones', '', '', 'Ones'])
    def test_play_game(self, mock_input):
        yahtzee_game = PlayYahtzee(num_players=1)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            yahtzee_game.play_game()
        self.assertIn("Game Over!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1 2 3', ''])
    def test_hold_dice_prompt(self, mock_input):
        player = PlayYahtzee(num_players=1).players[0]
        player.turn.dice_to_roll = [1, 3, 5]
        player.turn.get_state = MagicMock(return_value={'dice_values': [1, 2, 3, 4, 5]})
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            PlayYahtzee().hold_dice_prompt(player)
        self.assertEqual(player.turn.dice_to_roll, [])
        self.assertIn("Rolling dice", mock_stdout.getvalue())
        
    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()
