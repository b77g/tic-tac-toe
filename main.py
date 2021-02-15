from ttt import Board, Player, Game


def main():
    player_1 = Player('x')
    player_2 = Player('o')
    board = Board()

    GAME = Game(board, player_1, player_2)
    GAME.visualize()

    while GAME.active:
        print(f'{GAME.get_player()}\'s turn :: ', end='')
        inputs = GAME.get_player().get_move()

        if inputs in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            position = GAME.parse(int(inputs) - 1)
            if GAME.validate(*position):
                GAME.update(position)

        elif inputs == 'q':
            quit()


if __name__ == '__main__':
    main()
