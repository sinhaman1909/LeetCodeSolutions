class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.isupper() or word.istitle() or word.islower() else False