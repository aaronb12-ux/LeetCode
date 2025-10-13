class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def binary_search(potions_array, target_index):

            left = 0
            right = len(potions_array) - 1

            while left <= right:

                middle = (left + right) // 2

                if potions_array[middle] >= target_index:
                    right = middle - 1
                
                else:
                    left = middle + 1

            return left


        potions.sort()
        ans = []
        m = len(potions)
        
        for spell in spells:

            i = binary_search(potions, success / spell)

            ans.append(m - i) #number of valid potions
        
        return ans