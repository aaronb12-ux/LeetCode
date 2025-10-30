from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        #breadth first search
        #begin bfs at top left cell. 
            #check all directions and see if valid. if direction is valid add it to the queue
            #continue this same process for queue in main loop while the queue is full
            #if we find a path by the end (popped row and col is equal to 0,0)
            #if we make it out of the while loop return -1 
        n = len(grid)


        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n
        
        queue = deque([(0, 0, 1)]) #row, col, of current node. and number of steps taken from start to this spot
        visited = set([(0,0)]) #initially visit the first starting location
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1, -1), (-1, 1)]

        while queue:

            row, col, steps = queue.popleft()

            if (row, col) == (n - 1, n - 1): #made it to the end of the grid (bottom right)
                return steps
            
            for dx, dy in directions:

                new_row = row + dy
                new_col = col + dx
            
                if valid(new_row, new_col):
                    if (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, steps + 1))
        
        return -1
        
