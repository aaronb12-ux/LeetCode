'''

Find the Smallest Divisor Given a Threshold #1283:
Common solution space problem. We are given a set of values, 
and we need to find the max or min ‘x’ that makes certain conditions true. 
We begin by declaring our left and right pointers for the binary search. 
Min is set to 1 as that's the lowest possible divisor, and the max is set to the max value of the array.
We then perform our normal binary search. For each middle value, we test if that value is 
within our solution space (is_valid_divisor. If it is, then return true and test smaller 
values by updating the right pointer, otherwise update left pointer to test larger values. 
Since we return the smallest value, we return the left pointer at the end of the search. 

Algorithm: Binary search on solution space
Data Structures: array
Time Cmoplexity: O(n log(s)) where n is length of nums and s is highest value in solution space
'''


import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        #ceiling division when finding the sum with a given test value

        def is_valid_divisor(k):
            
            current_sum = 0

            for num in nums:

                current_sum = current_sum + math.ceil(num / k)
            
            return current_sum <= threshold
        

        left = 1
        right = max(nums)

        while left <= right:

            middle = (left + right) // 2

            if is_valid_divisor(middle):

                #test smaller values
                right = middle - 1
            
            else:

                left = middle + 1 #test larger values
        
        return left
