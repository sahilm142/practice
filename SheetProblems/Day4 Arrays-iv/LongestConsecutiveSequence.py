class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 1
        n = len(nums)
        if n==0 or n==1:
            return n
        
        nums.sort()
        start,end = 0,1
        k=1
        while k<n:
            if nums[k-1]+1==nums[k]:
                long = max(long, end-start+1)
                end+=1
            elif nums[k-1]==nums[k]:
                while k<n and nums[k-1]==nums[k]:
                    k+=1
                continue
            else:
                start = k
                end=k+1
            k+=1
        
        return long
            
        
