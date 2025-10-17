import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #sort piles
        #perform a binary search in range from (piles[0] - piles[-1]) and find num that is equal to h

        #we perform one binary search, but we calculate the hours taken for each value 'middle' during the binary search

        left = 1
        right = max(piles) 
        best = max(piles)
    
        def find_hours(k): #k is the number of bananas per hour we are testing

            num_hours = 0

            for pile in piles:

                hour_for_pile = math.ceil(pile / k)
                
                num_hours += hour_for_pile

            return num_hours
        

        while left <= right:

            k = (left + right) // 2  #number of bananas we plan to eat every hour

            hours_to_eat = find_hours(k) #finding hours it takes to eat all bananas at the above rate

            if hours_to_eat <= h:

                best = min(best, k)

                right = k - 1 #update right to test smaller values
            
            else: #if we are too slow -> need larger value

                left = k + 1
        
        return best

#Algorithm: binary search
#Data Structures: array
#Time Complexity: O(nlogw) where n is number of piles and w is the distance between max and min of the piles)
        
