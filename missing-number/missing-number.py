class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        for i in range(len(nums)+1):
            if i in hashmap:
                pass
            else:
                return i