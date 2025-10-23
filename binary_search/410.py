Split Array Largest Sum #410
Solution space binary search problem. This is known because we are “minimizing a max”. 
We first declare our left and right pointer where left = max(arr) and right = sum(arr). 
We then perform a binary search on this solution space. We have a helper function which we check for each middle. 
If this helper function returns true, then we know that ‘middle’ is valid, so we can check smaller values. 
And if the middle value returns false then check larger values. The helper function is the key logic in this problem. 
In this problem we need to check if we can create at most k subarrays where the sum of each subarray is at most middle. 
If we can do this in the function then return true. By the end of the binary search the left ptr will be pointing to our target value. 
We return left.

Time Complexity: O(n log(s)) where n is len(nums) and s is the greatest value in our solution space, so sum(arr)
Algorithms: Binary Search on Solution Space
Data Structures: array

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def condition_to_check(middle):

            arrays_created = 0
            curr_array = []

            for num in nums:

                curr_array.append(num)

                if sum(curr_array) > middle:
                    arrays_created += 1
                    curr_array = [num]
            
            if curr_array:
                arrays_created += 1
            
            return arrays_created <= k




        left = max(nums)
        right = sum(nums)

        while left <= right:

            middle = (left + right) // 2

            if condition_to_check(middle):

                right = middle - 1
            
            else:

                left = middle + 1
        
        return left
