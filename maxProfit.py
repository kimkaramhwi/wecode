def maxProfit(prices):
    maxprofit = 0
    length = len(prices)
    
    for i in range(length):
        for j in range(i+1, length):
            if prices[i] < prices[j]:
                maxprofit = max(maxprofit, prices[j] - prices[i])
    
    return maxprofit

prices = [6,5,4,3,2]
print(maxProfit(prices))