class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        if arr == sorted(arr, reverse=True) or arr == sorted(arr):
            return False
        
        max_element = max(arr)
        index_max = arr.index(max_element)
        if index_max == len(arr) - 1:
            return False
        
        for i in range(1, len(arr)):
            if i < index_max:
                if not arr[i] > arr[i-1]:
                    return False
            if i > index_max:
                if not arr[i-1] > arr[i]:
                    return False
                
        return True
                    