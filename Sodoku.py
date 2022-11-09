# initialize variable to hold n
n = 0

# open input file as 'f'
with open('sudoku9TB1.txt', 'r') as f:
    # read the first line in input file and save as n
    n = int(f.readline().strip())
    print(n)
    # save remainder of data to a variable
    data = f.readlines()
    print(data[0])

list = []
# remove every all teh spaces and cast each char into an int and save to a list
for i in range(n):
    for j in range(n):
        list.append(int(data[i][j * 2]))

# initialize 2d list
board = [[i for i in range(n)] for x in range(n)]
# create board from list
for i in range(n * n):
    board[int(i / n)][i % n] = list[i]
print(board)


class Sudoku:
    def __init__(self, board: [[]]):
        self.board = board
        self.n = len(board[0])

    # recursive method to solve sodoku

    def printBoard(self):
        print("---" * n)
        for i in range(n):
            print(board[i])
        print("---" * n)
    def isSolved(self):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    return False

        return True

    def get(self, position: int):
        return board[int(position / n)][position % n]

    def checker(self, location: int, value: int):
    # helper function to check if placing a certain number in a position is valid
        if value >n:
            return False

        current = board[int(location / n)][location % n]

        row = location % n
        col = int(location / n)
        #print("Suggestion =", value)
        #print("current =", current)
        #print("row =", row)
        #print("col =", col)

        # check row for value
        for i in range(n):
            if board[col][i] == value:
                return False

        # check col for value
        for i in range(n):
            if board[i][row] == value:
                return False

        # check box for value
        if row < 3:
            # box 1
            if col < 3:
                print("1.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j] == value:
                            return False
                return True

            # box 2
            elif col < 6:
                print('1.2')
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i+3][j] == value:
                            return False
                return True

            # box 3
            else:
                print("1.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i+6][j] == value:
                            return False
                return True

        elif row < 6:
            # box 4
            if col < 3:
                print("2.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j+3] == value:
                            return False
                return True

            # box 5
            elif col < 6:
                print("2.2")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j + 3] == value:
                            return False
                return True

            # box 6
            else:
                print("2.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 3] == value:
                            return False
                return True
        else:
            # box 6
            if col < 3:
                print("3.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j+6] == value:
                            return False
                return True

            # box 8
            elif col < 6:
                print("3.2")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i +3][j + 6] == value:
                            return False
                return True

            # box 9
            else:
                print("3.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 6] == value:
                            return False
                return True

    # method to print board easily
    def set(self, position: int, value: int):
        board[int(position/n)][position %n] = value

    def solve(self):
        #base case
        if self.isSolved():
            return
        else:
            for i in range(n*n):
                if self.get(i) == 0:
                    for j in range(1,10):
                        if self.checker(i, j):
                            self.set(i,j)
                            self.printBoard()
                            self.solve()



sud = Sudoku(board)
sud.printBoard()
sud.solve()


