from os import system, name


class Board:
    def __init__(self):
        self.state = [
            None, None, None,
            None, None, None,
            None, None, None
        ]

    def get_row(self, index):
        rows = ([], [], [])
        i = 0
        for row in rows:
            row.append(self.state[i])
            row.append(self.state[i + 1])
            row.append(self.state[i + 2])
            i += 3
        return rows[index]

    def get_column(self, index):
        columns = ([], [], [])
        i = 0
        for column in columns:
            column.append(self.state[i])
            column.append(self.state[i + 3])
            column.append(self.state[i + 6])
            i += 1
        return columns[index]

    def get_diagonal(self, index):
        diagonals = ([], [])
        if index in (0, 1):
            diagonals[0].append(self.state[0])
            diagonals[0].append(self.state[4])
            diagonals[0].append(self.state[8])
            diagonals[1].append(self.state[2])
            diagonals[1].append(self.state[4])
            diagonals[1].append(self.state[6])
            return diagonals[index]
        else:
            return (None, None, None)

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
            for item in self.state
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

    def validate(self, position):
        return self.board.state[position] == None

    def place(self, position):
        self.board.state[position] = self.get_player()

    def check_board(self):
        CHECKS = (
            self.board.get_row, self.board.get_column, self.board.get_diagonal
        )
        for check in CHECKS:
            for index in (0, 1, 2):
                if check(index).count(self.get_player()) == 3:
                    return f'{self.get_player()} won'
        if None not in self.board.state and self.active:
            return 'draw'

    def update(self, position):
        self.place(position)
        winner = self.check_board()
        self.active = False if winner else True
        self.visualize(winner)
        self.turn += 1

    def visualize(self, winner=None):
        system('clear') if name == 'posix' else system('cls')
        print(self.board)
        if winner:
            print(f'result :: {winner}')
