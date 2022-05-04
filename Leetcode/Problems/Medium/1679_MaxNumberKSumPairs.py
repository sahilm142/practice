#Sorting and 2-Pointers
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            total = nums[i]+nums[j]
            if total == k:
                cnt+=1
                i+=1
                j-=1
            elif total<k:
                i+=1
            elif total>k:
                j-=1
                
        return cnt

#using hashmap to store count
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        hm = {}
        
        for num in nums:
            res = k-num
            if res in hm and hm[res]>0:
                cnt+=1
                hm[res] -=1
            else:
                hm[num] = hm.get(num, 0)+1
                
        return cnt
        
