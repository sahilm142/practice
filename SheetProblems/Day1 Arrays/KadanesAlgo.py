class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algo
        #Create an array to store the max sum subarray to that index
        n = len(nums)
        dp = [None]*n
        maxx = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i]) #nums[i] + (dp[i-1] > 0 ? dp[i-1] : 0)
            maxx = max(maxx, dp[i])
        return maxx
            
        
