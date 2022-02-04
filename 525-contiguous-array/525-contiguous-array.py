class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        _sum = 0
        hashmap = {}
        
        for i in range(len(nums)):
            _sum = _sum + 1 if nums[i] == 1 else _sum - 1
            if _sum in hashmap:
                res = max(res, i - hashmap[_sum])
            else:
                hashmap[_sum] = i
                
            if _sum == 0:
                res = max(res, i + 1)
            
        return res
                
                
            
                