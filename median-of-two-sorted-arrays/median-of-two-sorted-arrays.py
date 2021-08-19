class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = float()
        for j in nums2:
            nums1.append(j)
        nums1.sort()  
        l = len(nums1)-1
        if len(nums1)%2==0:
           m = (nums1[l//2]+nums1[(l//2)+1])/2
        else:
            m = nums1[(l//2)]
        return m 
        