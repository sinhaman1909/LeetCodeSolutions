class Solution:
    def intToRoman(self, num: int) -> str:
        rom_dig = ''
        pre = {0: '', 1: 'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        place = 1
        
        while num:
            dig = num%10
            
            if (dig+1)%5==0:
                rom_dig = pre[place]+pre[(dig+1)*place] + rom_dig
            else:
                rom_dig = pre[dig//5*5*place] + dig%5*pre[place] + rom_dig 
                
            num = num//10
            place = place*10
            
        return rom_dig
        