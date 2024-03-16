# TODO Inherit from playground
class Player():
    def __init__(self, number):
        self.number = number
        if self.number == 1:
            self.sign = "x"
        else:
            self.sign = "o"

    def draw_sign(self, input, board):
        # TODO Check if input is valid
        column = ord(input[0].upper()) - 65
        row = int(input[1]) - 1
        # TODO Chech if coordinate has already a sign
        board.board[row][column] = f"{self.sign}"