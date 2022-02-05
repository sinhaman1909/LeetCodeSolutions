class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hashmap:
                return [hashmap[key], i]
            else:
                hashmap[nums[i]] = i
                
                