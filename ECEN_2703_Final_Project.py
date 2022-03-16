import numpy as np

def pos_move(x_position, y_position):
    move_x = (2, 1, 2, 1, -2, -1, -2, -1) #longitude movement of the knight
    move_y = (1, 2, -1, -2, 1, 2, -1, -2) #latitude movement of the knight
    possibilities = [] #initialize an empty list
    for i in range(8): # 8 ways a knight can move, we are iterating through that here
        if x_position + move_x[i] >= 0 and x_position + move_x[i] <= chess_board_size_int-1 and y_position + move_y[i] >=0 and y_position + move_y[i] <= chess_board_size_int-1 and chess_board[x_position+move_x[i]][y_position+move_y[i]] == 0:
          possibilities.append([x_position + move_x[i], y_position + move_y[i]]) 
          #checking if the next move is within the constraints and adding it to a list
    return possibilities



def solve_moves(x,y):
    counter = 2 # The very first number, 1 is already placed by the user and need to be incremented until it reaches 63
    total_it = chess_board_size_int*chess_board_size_int - 1 # example: for an 8x8 size board, total_it would be 63, only need to fill 63 more cells
    for i in range(total_it):
        possibility_count = pos_move(x,y) #the list of places the knight can go
        min = possibility_count[0] #min is the first element in the list
        for p in possibility_count: #iterating through the entire list
            if len(pos_move(p[0], p[1])) <= len(pos_move(min[0], min[1])): #calling pos_move again to get the count of 
                #how many possibilities would there be moving on to the next position 
                min = p #if the current iteration's count of possibilities is smaller than the count of the minimum, sets the new minimum
        x = min[0] #updates the x position
        y = min[1]  #updates the y position 
        chess_board[x][y] = counter #updates the chessboard, inserts the counter value
        counter += 1  #counter increases by 1

def print_board():
    for i in range(chess_board_size_int):
         
        for j in range(chess_board_size_int): #building the chessboard
            
            print("%5d"  %  (chess_board[i][j]), end = '|')
        print("\n")
        



# On the chessboard, (0,0) is the top left position and (8,8) is the bottom right position.
print("Welcome to Knight's Tour")
chess_board_size = input("Enter a number N, 5 or greater for the size of the chessboard N x N: ")
chess_board_size_int = int(chess_board_size)
if(chess_board_size_int < 5):
    print("The Knight's Tour cannot be completed with size: ", chess_board_size_int, "x", chess_board_size_int)
    exit()
print("Enter any number from 0 to", chess_board_size_int - 1, "for x position: ")
y = input("X position: ")
print("Enter any number from 0 to", chess_board_size_int - 1, "for y position: ")
x = input("Y position: ")
x_int = int(x)
y_int = int(y)

chess_board = []
for r in range(0, chess_board_size_int):
    chess_board.append([0 for c in range(0, chess_board_size_int)])





chess_board[x_int][y_int] = 1 #the first element 
solve_moves(x_int,y_int)  #calling solve_moves
print_board() #at the very end, print the board
