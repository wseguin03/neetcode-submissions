class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        board_dict = {}
        column_dict = {}
        square_dict = {}
        for num in range(n):
            board_dict[num] = {
                "row": set(),
                "column": set(),
                "box": set()            
                }
        for num in range(3):
            for c in range(3):
                board_dict[(num, c)] = set()
        #go row by row, make sets for rows, columns, and 3x3s, probably use a hash map to keep track?
        for i in range(n):
            row_set = set()
            row_count = 0
            col_count = 0
            box_count = 0
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in board_dict[i]["row"]:
                        return False
                    board_dict[i]["row"].add(board[i][j])
                    # row_count +=1
                    if board[i][j] in board_dict[(i//3, j//3)]:
                        return False
                    
                    board_dict[(i//3, j//3)].add(board[i][j])
                    
                if board[j][i] != '.':
                    if board[j][i] in board_dict[i]['column']:
                        return False
                    board_dict[i]["column"].add(board[j][i])
                    # col_count+=1
                
                
                
            # if row_count != len(board_dict[i]['row'] or col_count != len(board_dict[i]['column'])):
            #     return False
        return True