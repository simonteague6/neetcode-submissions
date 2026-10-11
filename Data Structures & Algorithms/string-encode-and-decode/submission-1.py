class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result = result + str + ":;"
        
        return result


    def decode(self, s: str) -> List[str]:

        strs = s.split(":;")
        strs.pop()
        return strs