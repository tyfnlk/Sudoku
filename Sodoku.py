
n = 0
data =[]

#open input file as 'f'
with open('sudoku9TB.txt', 'r') as f:
    #read the first line in input file and save as n
    n = int(f.readline().strip())
    print(n)
    file = f.readlines()
    print(file[0])


list =[]
for i in range(n):
    for j in range(n):
        list.append(int(file[i][j* 2]))

print(list)

class Board:
    def print(self,list[]):
        for i in range(n):
            for j in range(n):
                print(list[(9*i) +j])
        print("\n")

Board.print(list)




  
    




