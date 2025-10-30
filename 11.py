class Solution:
    def maxArea(self, height: List[int]) -> int:

        #declaring pointers
        left_ptr = 0 
        right_ptr = len(height) - 1

        #declaring answer variables
        ans = 0
        current_water = 0

        while left_ptr < right_ptr:

            current_water = (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr])

            ans = max(ans, current_water)

            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            elif height[right_ptr] < height[left_ptr]:
                right_ptr -= 1
            else:
                right_ptr -= 1
                left_ptr += 1
        
        return ans


#Data Structure: Array
#Algorithm: Two pointers
#Time Complexity: O(n)
#Space Complexity: O(n)
