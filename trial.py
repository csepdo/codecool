import os

# Creating a matrix.

description = 'This is a Sudoku game. The objective is to fill a 9×9 \ngrid with digits so that each column, each row, \nand each of the nine 3×3 boxes that compose \nthe grid contains all of the digits from 1 to 9. \nTo fill the board. you have to give the coordinates (row, column),\nand the digit you want to enter (e.g.: 0 1 2).\nIf you want to delete a digit, yout type 0 after the coordinates.\nThe coordinates 0 0 indicate the top left corner.'
col = 9
row = 9
e = ' '
board = [0] * col
for i in range(col):
    board[i] = [0] * row
solution = [0] * col
for j in range(col):
    solution[j] = [0] * row
    
# Gives the numbers of the Sudoku board.
def start():
    board[0] = [7, 8, 2, 6, 3, 9, 1, 4, 5]
    board[1] = [4, 6, 3, 5, 8, 1, 7, 2, 9]
    board[2] = [9, 5, 1, 7, 2, 4, 6, 8, 3]
    board[3] = [5, 3, 6, 1, 4, 2, 9, 7, 8]
    board[4] = [2, 9, 7, 3, 5, 8, 4, 1, 6]
    board[5] = [1, 4, 8, 9, 7, 6, 3, 5, 2]
    board[6] = [3, 1, 4, 8, 6, 5, 2, 9, 7]
    board[7] = [6, 2, 5, 4, 9, 7, 8, 3, 1]
    board[8] = [e, 7, 9, 2, 1, 3, 5, 6, 4]
    board_format()   

# Print out the Sudoku board in a readable foramt.
def board_format():
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[0]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[1]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[2]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[3]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[4]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[5]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[6]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[7]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[8]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    
# Modifies and re-prints the modified board.
def modify_board():  
    replace_number()
    os.system('cls' if os.name == 'nt' else 'clear')

# Check the numbers compared to the complete board.
def check_numbers():
    solution[0] = [7, 8, 2, 6, 3, 9, 1, 4, 5]
    solution[1] = [4, 6, 3, 5, 8, 1, 7, 2, 9]
    solution[2] = [9, 5, 1, 7, 2, 4, 6, 8, 3]
    solution[3] = [5, 3, 6, 1, 4, 2, 9, 7, 8]
    solution[4] = [2, 9, 7, 3, 5, 8, 4, 1, 6]
    solution[5] = [1, 4, 8, 9, 7, 6, 3, 5, 2]
    solution[6] = [3, 1, 4, 8, 6, 5, 2, 9, 7]
    solution[7] = [6, 2, 5, 4, 9, 7, 8, 3, 1]
    solution[8] = [8, 7, 9, 2, 1, 3, 5, 6, 4]
    if board == solution:
        print('Correct') 

# Makes the modification of the cells (insert, delete).
def replace_number():
    number_parameters = []
    number_parameters = [int(r) for r in input().split()]
    if board[number_parameters[0]][number_parameters[1]] == e:
        board[number_parameters[0]][number_parameters[1]] = number_parameters[2]
    elif number_parameters[2] == 0:
        board[number_parameters[0]][number_parameters[1]] = e

print(description)       
start()
while True:
    try:
        modify_board()
        board_format()
        check_numbers()
    except:
        IndexError

    