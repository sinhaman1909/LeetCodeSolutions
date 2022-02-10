class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s, count = 0, 0
        hashmap = {0:1}
        for n in nums:
            s += n
            if hashmap.get(s - k):
                count += hashmap[s - k]
            hashmap[s] = 1 + hashmap.get(s, 0)
            
        return count
            