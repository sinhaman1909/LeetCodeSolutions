class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                triplet = [nums[i],nums[l],nums[r]]
                if s<0:
                    l=l+1
                elif s>0:
                    r=r-1
                else:
                    if triplet not in ans:
                        ans.append(triplet)
                    l=l+1
                    r=r-1

        return ans
