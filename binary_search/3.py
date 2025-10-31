from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #sliding window
    

        #loop through the string with a right pointer. 
        #for each character, check if its value is '1' in our counts dictionary
        #if it is 1, then we need to pause the right pointer, and move the left one until we reach the first occurance of that character and remove it. we then continue. basically all counts should be when we are making the window (substring)
        if not s:
            return 0
        
        if len(s) == 1:
            return 1

        counts = defaultdict(int)
        ans = 0
        left = 0
        right = 0

        for right in range(len(s)):
            
            current_character = s[right] #get current character the right pointer is at
            counts[current_character] += 1

            while counts[current_character] > 1:

                counts[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
          
        
        return ans
