class Board():
    def __init__(self):
        self.size = 3
        self.board = []
        self.winner = ""
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("*")
            self.board.append(row)

    def draw_board(self):
        print(" |A|B|C|")
        for i in range(self.size):
            row = f"{i+1}|"
            for j in range(len(self.board[i])):
                row += self.board[i][j] + "|"
            print(row)
    
    def check_win_horizontal(self):
        row = ""
        for i in self.board:
            row = "".join(i)
            if row == "xxx":
                self.winner = "P1"
                return True
            elif row =="ooo":
                self.winner = "P2"
                return True
        return False

    def check_win_cross(self):
        row = ""
        for i in range(3):
            row += self.board[i][i]
        if row == "xxx":
            self.winner = "P1"
            return True
        elif row =="ooo":
            self.winner = "P2"
            return True
        return False
