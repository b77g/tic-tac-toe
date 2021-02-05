import unittest

from ttt import Board, Player, Game


# `TestGame` places the string representation of player objects
# instead of their instance, which makes tests more readable
class TestGame(Game):
    def __init__(self, board, player_1, player_2):
        super().__init__(board, player_1, player_2)

    def get_player(self):
        return str(self.player_1 if self.turn % 2 == 0 else self.player_2)


class Test(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player_1 = Player('x')
        self.player_2 = Player('o')
        self.game = TestGame(self.board, self.player_1, self.player_2)

    def test_row(self):
        self.game.turn = 8
        self.board.state = (
            'o', 'o', 'x',
            'x', 'x', 'x',
            'o', 'x', 'o'
        )
        self.assertEqual(self.game.check_board(), 'x won')

    def test_column(self):
        self.game.turn = 5
        self.board.state = (
            'o', None, 'x',
            'o', 'x', 'x',
            'o', None, None
        )
        self.assertEqual(self.game.check_board(), 'o won')

    def test_diagonal(self):
        self.game.turn = 6
        self.board.state = (
            'x', 'o', 'o',
            'o', 'x', 'x',
            None, None, 'x'
        )
        self.assertEqual(self.game.check_board(), 'x won')

    def test_draw(self):
        self.game.turn = 8
        self.board.state = (
            'x', 'o', 'x',
            'x', 'o', 'o',
            'o', 'x', 'x'
        )
        self.assertEqual(self.game.check_board(), 'draw')


if __name__ == '__main__':
    unittest.main()