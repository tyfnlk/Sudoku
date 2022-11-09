# initialize variable to hold n
n = 0

# open input file as 'f'
with open('sudoku9TB.txt', 'r') as f:
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
    def solve(self):
        pass

    def get(self, position: int):
        return board[int(position / n)][position % n]

    def checker(self, location: int, value: int):
        current = board[int(location / n)][location % n]

        row = location % n
        col = int(location / n)
        print(current)
        print("row =", row)
        print("col =", col)

        # check row for value
        for i in range(n):
            if board[col][i] == value:
                return False

        # check col for value
        for i in range(n):
            if board[int(i)][row] == value:
                return False

        # check box for value
        if row < 3:
            # box 1
            if col < 3:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j] == value:
                            return False
                return True

            # box 2
            elif col < 6:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j + 3] == value:
                            return False
                return True

            # box 3
            else:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j + 6] == value:
                            return False
                return True

        elif row < 6:
            # box 4
            if col < 3:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j] == value:
                            return False
                return True

            # box 5
            elif col < 6:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j + 3] == value:
                            return False
                return True

            # box 6
            else:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j + 6] == value:
                            return False
                return True
        else:
            # box 6
            if col < 3:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j] == value:
                            return False
                return True

            # box 8
            elif col < 6:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 3] == value:
                            return False
                return True

            # box 9
            else:
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 6] == value:
                            return False
                return True

    # method to print board easily
    def printBoard(self):
        for i in range(n):
            print(board[i])


sud = Sudoku(board)
sud.printBoard()
response = (sud.checker(78, 7))
print(response)

