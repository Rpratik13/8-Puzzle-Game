from Graph import *
from State import *


board = [[2, 8, 3],
         [1, 6, 4], 
         [7, 0, 5]]

final_state = [[1, 2, 3],
               [8, 0, 4],
               [7, 6, 5]]


if __name__ == '__main__':
    initialize()
   
    g = Graph()
    
    INITIAL_STATE = State(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]) 
    g.AstarTree(INITIAL_STATE)
    Screen().mainloop()