class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force
        max_so_far = 0
        for i in range(len(prices)):
            for j in range(len(prices)-1, i, -1):
                #print(max_so_far, prices[i], prices[j])

                if prices[i]<prices[j]:
                    max_so_far = max(max_so_far, prices[j]-prices[i])
        return max_so_far
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, res = prices[0], 0
        for i in range(1,len(prices)):
            res = max(res, prices[i]-min_so_far)
            min_so_far = min(min_so_far, prices[i])
            #res = max(res, prices[i]-min_so_far)
        return res

