class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1] , op = 6 
        # prices = [ 0 1 2 3 4 5 ]
        # have to be subtracting - sell - buy so in an example like p=[10,8,7,5,2]-> would lead to all -ve profits hence 0
        # brute force
        # constraints - buy - ideally a small number 
        # sell = always on rhs of buy - bcs u can only sell after buying , the largest num in arr so u have max profit
        l,r=0,0 # l = buy , r = sell
        maxP=0
        while (r < len(prices)): 
            # ascending = prices.sort() cant do sorting cuz itll mess up og order
            #  hv to check for profit
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else: #if buy > sold , then u should be at the end of the array
                l = r #cuz we found a rlly low price
            r+=1
        return maxP
            
