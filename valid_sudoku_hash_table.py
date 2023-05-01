from typing import List, Dict


def isValidSudoku(board: List[List[str]]) -> bool:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    group_types = ["row", "column", "square"]
    for type in group_types:
        for group_number in range(9):
            chunk = {digit:None for digit in digits}
            group = getGroup(board, type, group_number)
            for numb in group:
                if chunk.get(numb):
                    return False
                elif numb != ".":
                    chunk[numb] = True
    return True


def getGroup(board: List[List[str]], type: str, group_number: int) -> List:
    group = []
    if type == "row":
        group = board[group_number]
    elif type == "column":
        for i in range(9):
            group.append(board[i][group_number])
    elif type == "square":
        starting_row = group_number // 3
        starting_column = group_number % 3
        r_begin, r_end = starting_row*3, (starting_row + 1)*3
        c_begin, c_end = starting_column*3, (starting_column + 1)*3
        for i in range(r_begin, r_end):
            for j in range(c_begin, c_end):
                group.append(board[i][j])
    return group




board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

def main():
    print(isValidSudoku(board))


main()