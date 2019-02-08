# 79. Word Search

class Solution:
    
    def searching(self, x, y, board, word, curr, visited):
        # curr: current letter of the word
        # visited: save visited position for backtracking
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # coordinates of the neighbors
        
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or board[x][y] != word[curr]:
            return False
    
        if curr == len(word) - 1:
            return True
        
        visited.add((x, y))
        for d in range(4):
            # searching around the neighbor of current position
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) not in visited:
                if self.searching(nx, ny, board, word, curr + 1, visited):
                    return True
        visited.discard((x, y))
        return False
                
            
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':

        for x in range(len(board)):
            for y in range(len(board[0])):
                visited = set()
                if self.searching(x, y, board, word, 0, visited ):
                    return True
        return False