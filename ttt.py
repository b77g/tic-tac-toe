from os import system, name


class Board:
    def __init__(self):
        self.state = (
            [None, None, None],
            [None, None, None],
            [None, None, None]
        )

    def get_row(self, index):
        return tuple(self.state[index])

    def get_column(self, index):
        return (
            self.state[0][index],
            self.state[1][index],
            self.state[2][index]
        )

    def get_diagonal(self, index):
        if index == 0:
            return (
                self.state[0][0],
                self.state[1][1],
                self.state[2][2]
            )
        elif index == 1:
            return (
                self.state[0][2],
                self.state[1][1],
                self.state[2][0]
            )
        else:
            return (None, None, None)

    def flat_board(self):
        return tuple(item for list in self.state for item in list)

    def __str__(self):
        TEMPLATE = (
            '+---------+    +---------+\n'
            + '| {}  {}  {} |    | 1  2  3 |\n'
            + '| {}  {}  {} |    | 4  5  6 |\n'
            + '| {}  {}  {} |    | 7  8  9 |\n'
            + '+---------+    +---------+\n'
        )
        format_string = (
            item if item != None else '.'
            for item in self.flat_board()
        )
        return TEMPLATE.format(*format_string)


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        return input().strip().lower()

    def __repr__(self):
        return self.letter


class Game:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.active = True
        self.turn = 0

    def get_player(self):
        return self.player_1 if self.turn % 2 == 0 else self.player_2

    def parse(self, position):
        return {
            0: (0, 0), 1: (0, 1), 2: (0, 2),
            3: (1, 0), 4: (1, 1), 5: (1, 2),
            6: (2, 0), 7: (2, 1), 8: (2, 2)
        }.get(position)

    def validate(self, x, y):
        return self.board.state[x][y] == None

    def place(self, x, y):
        self.board.state[x][y] = self.get_player()

    def check_board(self):
        CHECKS = (
            self.board.get_row, self.board.get_column, self.board.get_diagonal
        )
        for check in CHECKS:
            for index in (0, 1, 2):
                if check(index).count(self.get_player()) == 3:
                    return f'{self.get_player()} won'
        if None not in self.board.flat_board() and self.active:
            return 'draw'

    def update(self, position):
        self.place(*position)
        winner = self.check_board()
        self.active = False if winner else True
        self.visualize(winner)
        self.turn += 1

    def visualize(self, winner=None):
        system('clear') if name == 'posix' else system('cls')
        print(self.board)
        if winner:
            print(f'result :: {winner}')
