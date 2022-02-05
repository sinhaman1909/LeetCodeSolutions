class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            key = target - numbers[i]
            if key in hashmap:
                return [hashmap[key] + 1, i + 1]
            else:
                hashmap[numbers[i]] = i
            