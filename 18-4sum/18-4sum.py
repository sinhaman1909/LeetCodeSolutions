class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    if s > target:
                        r -= 1
                    if s == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return res
        