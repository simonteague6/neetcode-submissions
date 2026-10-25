from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        right = 0
        chars = defaultdict() # "d" : 3 (index of d) 

        while right < len(s):
            current_char = s[right]
            if current_char not in chars.keys():
                chars[current_char] = right #first assign
            else:
                left = max(left, chars[current_char] + 1) #update left pointer to 1 past the newest occurence
                chars[current_char] = right #reassign

            maxLen = max(maxLen, right - left+1)
            right += 1
        return maxLen