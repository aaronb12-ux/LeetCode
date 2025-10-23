class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        #dfs and binary search

        #run a binary search in values between range: 0 max(height)

        #for each value run a dfs and check if we can construct a valid path
        m = len(heights) #num rows
        n = len(heights[0]) #num cols

        def valid(row, col):

            return 0 <= row < m and 0 <= col < n
        
        def depth_first_search(effort):

            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            seen = {(0,0)}
            stack = [(0,0)]

            while stack:

                row, col = stack.pop()

                if (row, col) == (m - 1, n - 1):
                    return True #acceptable path -> continue binary search to look for smaller 'effort'
                
                for dx, dy in directions:

                    next_row = row + dy
                    next_col = col + dx

                    if valid(next_row, next_col) and (next_row, next_col) not in seen:

                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            return False
        
        left = 0
        right = max(max(row) for row in heights)

        while left <= right:

            middle = (left + right) // 2

            if depth_first_search(middle):
                right = middle - 1
            else:
                left = middle + 1
        
        return left
    

#Algorithms: DFS, Binary Search
#Data Structures: Stack, Array
#Time Complexity: O(m * n * logK) where m is num rows, n num cols, and k is max value in entire 2d array
