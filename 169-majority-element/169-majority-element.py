class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        
        for n in nums:   
            hashmap[n] = 1 + hashmap.get(n, 0)
            if hashmap[n] > len(nums) // 2:
                return n 
        