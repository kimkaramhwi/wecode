class Solution:
    def maxProfit(self, prices) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

    print(maxProfit(prices= [3,1,4,8,18]))