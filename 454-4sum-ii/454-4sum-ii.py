class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        hashmap = {}
        for num1 in nums1:
            for num2 in nums2:
                hashmap[num1 + num2] = 1 + hashmap.get(num1 + num2, 0)
        
        for num3 in nums3:
               for num4 in nums4:
                    key = -(num3 + num4)
                    if key in hashmap:
                        res += hashmap[key]
                            
        return res