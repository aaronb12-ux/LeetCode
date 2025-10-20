import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        
        def get_total_hours(middle): #middle is the current kph we are testing for the trains

            curr = 0
            
            for index, distance in enumerate(dist):

                if index == len(dist) - 1: #at final index. DONT round to nearest hour

                    curr = curr + (distance / middle)

                else: #otherwise find the time for the train, then round to highest int to account for wait time

                    curr = curr + math.ceil(distance / middle) 
            
            return curr <= hour


        #when is it impossible to arrive on time?


        left = 1
        right = 10**7

        while left <= right:

            middle = (left + right) // 2

            #total_hours = get_total_hours(middle)

            if get_total_hours(middle):

                #check smaller vals

                right = middle - 1
            
            else:
                left = middle + 1
        

        return left if left <= 10**7 else -1
    

#Algorithm: Binary Search on solution space
#Data Structures:array
#Time Complexity: O(N * Log(right)) where N == number of trains and right is the max value of the binary search check
