#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bp):
    find = find_empty(bp)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bp, i, (row, col)):
            bp[row][col] = i

            if solve(bp):
                return True

            bp[row][col] = 0

    return False

def valid(bp, num, pos):
    #check row
    for i in range(len(bp[0])):
        if bp[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bp)):
        if bp[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_y*3 + 3):
            if bp[i][j] == num and (i,j) != pos:
                return False
    return True

def board_print(bp):
    for i in range(len(bp)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")

        for j in range(len(bp[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bp[i][j])
            else:
                print(str(bp[i][j]) + " ", end="")

def find_empty(bp):
    for i in range(len(bp)):
        for j in range(len(bp[0])):
            if bp[i][j] == 0:
                return (i, j)
    return None

board_print(board)
solve(board)
print("_______________________")
board_print(board)

