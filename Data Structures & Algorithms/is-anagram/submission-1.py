class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(26):
            if s.count(chr(i+97)) != t.count(chr(i+97)):
                return False

        return True