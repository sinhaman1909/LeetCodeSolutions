class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
            
        return res
                
                
