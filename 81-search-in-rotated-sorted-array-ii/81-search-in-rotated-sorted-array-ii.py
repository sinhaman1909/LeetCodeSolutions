class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for element in nums:
            if element == target:
                return True
        return False