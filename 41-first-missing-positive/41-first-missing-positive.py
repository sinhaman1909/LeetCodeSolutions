class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        answer = 1
        while answer in hashset:
            answer += 1
        return answer
        
        
