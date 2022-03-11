def maxProfit(prices):
    min_num = prices.index(min(prices)) # 가장 작은 숫자의 인덱스를 찾는다
    my_list = prices[min_num:] # 가장 작은 숫자부터 인덱스를 끊어서 새로 생성
    return max(my_list) - min(my_list)

prices = [3,2,1,5,6]
print(maxProfit(prices))