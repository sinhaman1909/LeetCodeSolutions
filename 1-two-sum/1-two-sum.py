class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hashmap:
                res.append(hashmap[key])
                res.append(i)
                return res
            else:
                hashmap[nums[i]] = i
                
                