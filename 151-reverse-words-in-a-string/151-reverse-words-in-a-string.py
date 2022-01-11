class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        #length = len(s)
        spaces = [' ']
        
        i = 0
        
        while i < len(s):
            if s[i] not in spaces:
                word_start = i
                while i < len(s) and s[i] not in spaces:
                    i+=1
                word.append(s[word_start:i])
            i+=1
        return " ".join(reversed(word))
        
        