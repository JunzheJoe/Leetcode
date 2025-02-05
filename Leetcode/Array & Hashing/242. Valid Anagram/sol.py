# class Solution:
    # def isAnagram(self, s: str, t: str) -> bool: 
        # return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # Create two hashmaps (char -> counts) and see if they are equal