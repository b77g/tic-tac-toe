import unittest
from ttt import Board, Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game()

    def test_row(self):
        self.board.state = [
            'o', 'o', 'x',
            'x', 'x', 'x',
            'o', 'x', 'o'
            ]
        self.game.turn = 8
        result = self.game.check(self.board)
        self.assertEqual(result, 'x won')

    def test_col(self):
        self.board.state = [
            'o', None, 'x',
            'o', 'x', 'x',
            'o', None, None
            ]
        self.game.turn = 5
        result = self.game.check(self.board)
        self.assertEqual(result, 'o won')

    def test_diag(self):
        self.board.state = [
            'x', 'o', 'o',
            'o', 'x', 'x',
            None, None, 'x'
            ]
        self.game.turn = 6
        result = self.game.check(self.board)
        self.assertEqual(result, 'x won')

    def test_draw(self):
        self.board.state = [
            'x', 'o', 'x',
            'x', 'o', 'o',
            'o', 'x', 'x'
            ]
        self.game.turn = 8
        result = self.game.check(self.board)
        self.assertEqual(result, 'draw')

if __name__ == '__main__':
    unittest.main()
