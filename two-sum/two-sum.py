class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,1
        indices = []
        while r < len(nums):
            if nums[l] + nums[r]==target:
                indices.append(l)
                indices.append(r)
                return indices
            r+=1
            if r==len(nums):
                l+=1
                r=l+1
        return indices