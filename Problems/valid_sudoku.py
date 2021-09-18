class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if not self.is_valid(board, r, c):
                    return False
        return True
    
    def is_valid(self, board, row, col):
        return self.is_valid_row(board, row) and self.is_valid_col(board, col) and self.is_valid_box(board, row - row % 3, col - col % 3)
    
    def is_valid_row(self, board, row):
        set_ = set()
        
        for i in range(0, 9):
            if board[row][i] in set_:
                return False
            
            if board[row][i] != ".":
                set_.add(board[row][i])
                
        return True
    
    def is_valid_col(self, board, col):
        set_ = set()
        
        for i in range(0, 9):
            if board[i][col] in set_:
                return False
            
            if board[i][col] != ".":
                set_.add(board[i][col])
                
        return True
    
    
    def is_valid_box(self, board, row, col):
        set_ = set()
        
        for r in range(0, 3):
            for c in range(0, 3):
                current_cell = board[row+r][col+c]
                
                if current_cell in set_:
                    return False
                
                if current_cell != ".":
                    set_.add(current_cell)
                    
        return True
