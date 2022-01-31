class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = -float(inf)
        for customer_wealth in accounts:
            if sum(customer_wealth) > _max:
                _max = sum(customer_wealth)
            
        return _max
        