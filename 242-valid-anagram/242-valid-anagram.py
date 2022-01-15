class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        cursor = 0
        while cursor < len(s):
            if s[cursor] != t[cursor]:
                return False
            cursor += 1
        return True