# 51. N-Queens

class Solution:
    
    def isValid(self, prev_cols, curr_col, curr_row):
        for prev_row in range(curr_row):
            if prev_cols[prev_row] == curr_col or curr_row - prev_row == abs(prev_cols[prev_row] - curr_col):
                return False
        return True
            
    def backTrack(self, ans, pos, row, n):
        if row == n:
            ans.append(['.'* p + 'Q' + '.'*(n-1-p) for p in pos])
            return
        for col in range(n):
            if self.isValid(pos, col, row):
                pos.append(col)
                self.backTrack(ans, pos, row + 1, n)
                pos.pop()
        return
        
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        ans, pos = [], []
        self.backTrack(ans, pos, 0, n)
        return ans