from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) 
        # initializes new keys with value [] so that you can append to a new key 

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(str)
        
        return list(result.values())