
'''
Divide Chocolate #1231
Solution space binary search problem. 
This problem requires us to maximize the minimum value in the solution space. 
We need to run a binary search on the solution space, then for each ‘middle’ value we check if it meets the condition. 
If we return true of this condition we check LARGER values by updating the left pointer, 
otherwise check smaller values by updating the right pointer. Now, we create a 
helper function create_pieces(middle) which takes a parameter middle which is a sweetness. 
In this function we need to see if we can create k + 1 pieces where each piece is AT LEAST middle. 
If this can be done, return True. By the end of the binary search we return the right pointer because 
this will be pointing to the max value in the solution space. 
This problem requires a binary search algorithm, an array data structure, and is run is O(n logs) 
time where n is the length of ‘sweetness’ and s is the max value in our solution space
'''

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        if len(sweetness) == k + 1: #base case
            return min(sweetness)
        
        def create_pieces(middle):
            pieces_made = 0
            current_sweetness = 0
            #need to divide chocolate and test if all values have at least 'k' sweetness
            for val in sweetness:
                
                current_sweetness = current_sweetness + val

                if current_sweetness >= middle:

                    pieces_made = pieces_made + 1
                    current_sweetness = 0
            
       
            return pieces_made >= k + 1
                

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)

        while left <= right:

            middle = (left + right) // 2

            if create_pieces(middle): #want to check LARGER values now
                
                left = middle + 1

            else:

                right = middle - 1
        
        return right
    
