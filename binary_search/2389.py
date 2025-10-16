class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        
        #declare vars and data structures needed
        nums.sort()
        prefix_sum = [nums[0]]
        ans = []


        #build prefix sum
        for i in range(1, len(nums)):

            prefix_sum.append(prefix_sum[-1] + nums[i])


        #binary search implemented on each query
        def binary_search(query):

            left = 0
            right = len(nums) - 1

            while left <= right:

                middle = (left + right) // 2

                if prefix_sum[middle] == query:

                    return middle + 1
                
                elif prefix_sum[middle] < query:

                    left = middle + 1
                
                else:
                    right = middle - 1
            
            return left
        
        #finding subarr for each query
        for query in queries:
            ans.append(binary_search(query))
        
        return ans
    

#Algorithms: Prefix Sum, Binary Search
#Data Structures: Array
#Time Complexity: O(nlogn + mlogn) where O(nlogn) is sorting array initially and O(mlogn) is the binary search for the query array, which is m
        