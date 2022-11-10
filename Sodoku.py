"""
Terry Leeshanok
COSC 3117
ID#229685780
Assignment 4
"""
# initialize variable to hold n
n = 0

#ask user for file to import
filename = input("enter file name ")

#save new file name for export later
fileout = filename.replace(".txt","Solution.txt")

# open input file as 'f'
with open(filename, 'r') as f:

    # read the first line in input file and save as n
    n = int(f.readline().strip())
    # save remainder of data
    data = f.readlines()


list = []
# remove every all the spaces and cast each char into an int and save to a list
for i in range(n):
    for j in range(n):
        list.append(int(data[i][j * 2]))

# initialize 2d list
board = [[i for i in range(n)] for x in range(n)]
# create board from list
for i in range(n * n):
    board[int(i / n)][i % n] = list[i]

#creat sudoku class
class Sudoku:
    def __init__(self, board: [[]]):
        #save board
        self.board = board
        #get n from board
        self.n = len(board[0])
        #success tracker
        self.success = 0
        self.solved =[]
        #exit if n not 9
        if self.n != 9:
            print("invalid board")
            SystemExit()
        print("puzzle")
        self.printBoard()


#function to print board easily
    def printBoard(self):
        print("---" * n)
        for i in range(n):
            print(board[i])
        print("---" * n)

#function to check if board is solved
    def isSolved(self):

        for x in range(n * n):
            if self.get(x) == 0:
                return False
        return True

#function to return value of any position
    def get(self, position: int):
        return board[int(position / n)][position % n]

#function to check if a value can be placed in a location
    def checker(self, location: int, value: int):
        #check if value is between 1 and n
        if value > n or value < 1:
            return False

        #convert int into row and col correspondent
        row = location % n
        col = int(location / n)

        # check if value already exists in the row
        for i in range(n):
            if board[col][i] == value:
                return False

        # check if value already exists in col
        for i in range(n):
            if board[i][row] == value:
                return False

        # check if value is already in respective 3x3 box
        if row < 3:
            # box 1
            if col < 3:
                #print("1.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j] == value:
                            return False
                return True

            # box 2
            elif col < 6:
                #print('1.2')
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j] == value:
                            return False
                return True

            # box 3
            else:
                #print("1.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j] == value:
                            return False
                return True

        elif row < 6:
            # box 4
            if col < 3:
                #print("2.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j + 3] == value:
                            return False
                return True

            # box 5
            elif col < 6:
                #print("2.2")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j + 3] == value:
                            return False
                return True

            # box 6
            else:
                #print("2.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 3] == value:
                            return False
                return True
        else:
            # box 6
            if col < 3:
                #print("3.1")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i][j + 6] == value:
                            return False
                return True

            # box 8
            elif col < 6:
                #print("3.2")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 3][j + 6] == value:
                            return False
                return True

            # box 9
            else:
                #print("3.3")
                for i in range(int(n / 3)):
                    for j in range(int(n / 3)):
                        if board[i + 6][j + 6] == value:
                            return False
                return True

    # method to set value in position
    def set(self, position: int, value: int):
        board[int(position / n)][position % n] = value

    #recursive function to solve sudoku
    def solve(self):
        # base case
        #when solved print board and output to file
        if self.isSolved():
            print("Solution")
            self.printBoard()
            self.solved =self.board
            self.success =1
            #output solution to file
            self.output()
            return
        #iterate through each position
        for i in range(n * n):
            #check if the position is unfilled
            if self.get(i) == 0:
                #iterate through all possible inputs
                for j in range(1, 10):
                    #check if input is valid for position using helper function(checker)
                    if self.checker(i, j):
                        #set value j in position i
                        self.set(i, j)
                        #recursive call
                        self.solve()
                    #if recursive call fails, backtrack by resetting position i
                    self.set(i, 0)
                return



    #output function to easily write state of board to file
    def output(self):
        # open file with file name derived from original input file
        with open(fileout, 'w') as out:
            # nested for loop to iterate through 2d list
            for y in range(n):
                for z in range(n):
                    # write each value
                    out.write(str(self.board[y][z]))
                    # add space after each value
                    out.write(" ")
                # skip line after each row is completed
                out.write("\n")

#create sudoku instance
sud = Sudoku(board)
#call solve function
sud.solve()
#write output in fail case
if sud.success == 0:
    print("there is no solution")
    with open(fileout, 'w') as out:
        out.write("-1")


