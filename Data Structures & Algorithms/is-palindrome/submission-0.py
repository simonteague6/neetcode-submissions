class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()
        
        
        new_str_reversed = new_str[::-1]

        return new_str == new_str_reversed