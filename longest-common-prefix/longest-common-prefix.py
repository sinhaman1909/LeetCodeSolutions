class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while not(strs[i].startswith(prefix)):
                prefix = prefix[:len(prefix)-1]
        return prefix
                
            