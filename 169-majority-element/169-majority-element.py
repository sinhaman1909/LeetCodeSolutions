class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = {}
        for element in nums:
            if element in freqCount.keys():
                freqCount[element] = freqCount[element] + 1
            else:
                freqCount[element] = 1
        
        for key in freqCount.keys():
            if freqCount[key] > len(nums) // 2:
                return key