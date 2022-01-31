class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = -float(inf)
        for customer_wealth in accounts:
            _max = max(_max, sum(customer_wealth))
            
        return _max
        