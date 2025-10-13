def searchInsert(nums, target):

    left = 0
    right = len(target) - 1

    while left <= right:

        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        
        elif target > nums[middle]:

            left = middle + 1

        else:

            right = middle - 1
    
    return left



#Algorithm: Binary Search
#Data Structures: Array
#Time Complexity: O(logn)