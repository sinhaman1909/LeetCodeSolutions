class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for i in s:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for j in t:
            if hashmap.get(j):
                hashmap[j] -= 1
            else:
                return j