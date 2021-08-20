# Most Profit from selling stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 
```
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.
```


My solution: 
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = max(prices) 
        profit = 0
        start = 0
        
        while start < len(prices) - 1:
            delta = 0 
            potential = 0
            buy_price = prices[start]
            sell_idx = start + 1
            last = start 
            
            if buy_price == highest:
                start += 1
                continue
                
            while delta >= 0 and sell_idx < len(prices): 
                delta = prices[sell_idx] - prices[last] 
                
                if delta <= 0:
                    delta = -1
                    start = sell_idx
                    continue
                    
                if (prices[sell_idx] - buy_price) > potential:
                    potential = prices[sell_idx] - buy_price
                    
                last = sell_idx
                sell_idx += 1
                
            start = sell_idx
            profit += potential
        
        return profit
```

Clever algo:
```python
# there were faster solutions than this one, but I enjoyed the simplicity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
```
