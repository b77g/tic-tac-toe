from os import system, name

def clear():
    system('clear') if name == 'posix' else system('cls')

class Board:
    def __init__(self):
        self.state = [
            None, None, None,
            None, None, None,
            None, None, None
            ]

    def rows(self, index):
        rows = ([], [], [])
        i = 0
        for row in rows:
            row.append(self.state[i])
            row.append(self.state[i + 1])
            row.append(self.state[i + 2])
            i += 3
        return rows[index]

    def columns(self, index):
        columns = ([], [], [])
        i = 0
        for column in columns:
            column.append(self.state[i])
            column.append(self.state[i + 3])
            column.append(self.state[i + 6])
            i += 1
        return columns[index]

    def diagonals(self, index):
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
            return [None, None, None]

    def __str__(self):
        TEMPLATE = '''+---------+    +---------+
| {}  {}  {} |    | 1  2  3 |
| {}  {}  {} |    | 4  5  6 |
| {}  {}  {} |    | 7  8  9 |
+---------+    +---------+
'''
        draw = []
        for i in self.state:
            if i == None:
                draw += '.'
            else:
                draw += i
        return TEMPLATE.format(
            draw[0], draw[1], draw[2],
            draw[3], draw[4], draw[5],
            draw[6], draw[7], draw[8],
            )

class Game:
    def __init__(self):
        self.active = True
        self.turn = 0

    def player(self):
        return 'x' if self.turn % 2 == 0 else 'o'

    def validate(self, board, position):
        return board.state[position] == None

    def place(self, board, position):
        board.state[position] = self.player()

    def check(self, board):
        CHECKS = (board.rows, board.columns, board.diagonals)
        for check in CHECKS:
            for index in (0, 1, 2):
                if check(index).count(self.player()) == 3:
                    self.active = False
                    return f'{self.player()} won'
        if None not in board.state and self.active:
            self.active = False
            return 'draw'

    def update(self, board, position):
        self.place(board, position)
        winner = self.check(board)
        self.visualize(board, winner)
        self.turn += 1

    def visualize(self, board, winner=None):
        clear()
        print(board)
        if winner:
            print(f'result :: {winner}')

def main():
    board = Board()
    game = Game()
    game.visualize(board)

    while game.active:
        inputs = input(f'{game.player()}\'s turn :: ').strip().lower()

        if inputs in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if game.validate(board, position := int(inputs) - 1):
                game.update(board, position)
        elif inputs == 'q':
            quit()

if __name__ == '__main__':
    main()
