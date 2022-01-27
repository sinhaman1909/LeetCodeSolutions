from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, binary):
        cur = self.root
        for char in binary:
            cur = cur.children[int(char)]
    
    def search(self, binary) -> int:
        result = 0
        cur = self.root
        for char in binary:
            opposite = 1 - int(char)
            if opposite in cur.children:
                result = (result << 1) | 1
                cur = cur.children[opposite]
            else:
                result = (result << 1)
                cur = cur.children[int(char)]
        return result

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        result = float('-inf')
        maxLen = len(bin(max(nums))[2:]) # format binary string in length of  max num
        for num in nums:
            key = bin(num)[2:].zfill(maxLen)
            trie.insert(key)
            result = max(result, trie.search(key))
        return result