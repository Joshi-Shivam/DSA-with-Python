class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        min=float("inf")
        profit=0
        idx=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
                print("New min found",min)
            profit=prices[i]-min
            print("Current profit",profit)
            if profit>max:
                max=profit
                idx=i+1
        print("idx is ",idx)
        print(f"Profit is {profit} max is {max}")
        return max



            

       
