class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        d = {}
        for i in range(0,len(nums)):
            key = target - nums[i]
            if key in d:
                l.append(d[key])
                l.append(i)
                return l
            d[nums[i]] = i
            
                        
        