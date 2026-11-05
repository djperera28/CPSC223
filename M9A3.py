## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 9 Assignment 3

def print_board(nested_list):
    border = "-" * (2 * len(nested_list[0]) + 1)
    for row in nested_list:
        print(border)
        print("|" + "|".join(row) + "|")
    print(border)

#hard code
board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]
print_board(board1_list)
print() #just for a spacer line
board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]
print_board(board2_list)
print() #just for a spacer line
board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]
print_board(board3_list)
