class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        min=float("inf")
        profit=0
        idx=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            profit=prices[i]-min
            if profit>max:
                max=profit
                idx=i+1
        return max



            

       
