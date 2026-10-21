class Solution:
    def alphaNum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        # while odd case or even case
        while left < right:

            # ensure alpha numeric
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            # check
            if s[left].lower() != s[right].lower():
                return False
                

            # increment left and right
            left += 1
            right -= 1

            

        return True

