import unittest
from unittest.mock import patch
from game import Game

class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['quit'])
    def test_game_quit(self, mock_input):
        game = Game()
        game.start()

        self.assertEqual(mock_input.call_count, 1)

    @patch('builtins.input', side_effect=['look', 'quit'])
    def test_game_look_and_quit(self, mock_input):
        game = Game()
        game.start()

        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=['go east', 'quit'])
    def test_game_go_and_quit(self, mock_input):
        game = Game()
        game.start()

        self.assertEqual(mock_input.call_count, 2)



    @patch('builtins.input', side_effect=['invalid_command', 'quit'])
    def test_game_invalid_command_and_quit(self, mock_input):
        game = Game()
        game.start()

        self.assertEqual(mock_input.call_count, 2)

if __name__ == '__main__':
    unittest.main()
