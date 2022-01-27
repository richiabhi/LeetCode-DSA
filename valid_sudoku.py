def sudoku(board):
    row, col, block = set(), set(), set()
    for i in range(9):
        for j in range(9):
            if(board[i][j] != '.'):
                rkey = (i, board[i][j])
                ckey = (j, board[i][j])
                bkey = (i//3, j//3, board[i][j])
                if((rkey in row) or (ckey in col) or (bkey in block)):
                    return False
                row.add(rkey)
                col.add(ckey)
                block.add(bkey)
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sudoku(board))
