from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        
        m = len(mat) #num rows
        n = len(mat[0]) #num cols
        seen = set()
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)] #right, left, up, down

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
            
        def initializeQueue():
            for row in range(m): #initially fill queue with 0's
                for col in range(n):
                    if mat[row][col] == 0:
                        queue.append((row, col, 0))
                        seen.add((row, col))

        def bfs():
            while queue:
                row, col, steps = queue.popleft()
                for dx, dy in directions:
                    next_row = row + dy
                    next_col = col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        queue.append((next_row, next_col, steps + 1))
                        seen.add((next_row, next_col))
                        mat[next_row][next_col] = steps + 1
        
        initializeQueue()
        bfs()


        return mat
