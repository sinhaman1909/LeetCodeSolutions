class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = {}
        for element in nums:
            if element not in freqCount.keys():
                freqCount[element] = 1
            else:
                freqCount.update({ element : freqCount[element] + 1})
                if freqCount[element] > len(nums) // 2:
                    return element
        return element