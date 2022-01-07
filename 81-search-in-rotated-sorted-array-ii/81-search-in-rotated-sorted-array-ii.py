class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for index in range(len(nums)):
            if nums[index] == target:
                return True
        return False