class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        keyCount = {}
        curr = 0
        while curr < len(nums):
            element = nums[curr]
            if element in keyCount and keyCount[element] >= 2:
                nums.remove(element)
                keyCount[element] += 1
            elif element in keyCount:
                keyCount[element] += 1
                curr += 1
            else:
                keyCount[element] = 1
                curr += 1
        return len(nums)
        