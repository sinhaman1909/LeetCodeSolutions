class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = {}
        ans = []
        
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for key in hashMap.keys():
            if hashMap[key] == 1:
                ans.append(key)
        
        return ans