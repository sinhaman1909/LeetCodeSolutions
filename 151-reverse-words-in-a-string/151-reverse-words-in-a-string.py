class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        result = ""
        for index in range(len(word_list) - 1, -1, -1):
            result = result + word_list[index]
            result = result.strip() + " "
        return result[:-1]
        
        