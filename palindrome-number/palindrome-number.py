class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = ""
        n = x
        if x == 0:
            return True
        while x > 0:
            temp = x%10
            s = s + str(temp)
            x = x//10
        n = str(n)
        if s == n:
            return True
        else:
            return False
        
        
        