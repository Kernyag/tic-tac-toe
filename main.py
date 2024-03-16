import board
import player

MAX_MOVE = 10

playground = board.Board()
playground.draw_board()

p1 = player.Player(number=1)
p2 = player.Player(number=2)

isGameOver = False
cnt = 1
while not isGameOver:
    if cnt % 2 != 0:
        move = input(f"Player 1 move: ")
        p1.draw_sign(move, playground)
    else:
        move = input(f"Player 2 move: ")
        p2.draw_sign(move, playground)
    playground.draw_board()
    cnt += 1
    if playground.check_win_horizontal() or playground.check_win_cross() or cnt == MAX_MOVE:
        isGameOver = True

    if playground.winner == "P1":
        print("Player 1 won the game")
    elif playground.winner == "P2":
        print("Player 2 won the game")
    else:
        print("Draw")
    
    # TODO promt if want do play again