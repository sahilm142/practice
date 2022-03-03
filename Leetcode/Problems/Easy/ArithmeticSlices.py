class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #Brute Force
        #Traversing after checking diff b/w i, i+1, i+2
        count = 0
        n = len(nums)
        for i in range(n-2):
            diff = nums[i+1]-nums[i]
            diff2 = nums[i+2]-nums[i+1]
            if diff==diff2:
                count+=1
                for j in range(i+3,n):
                    diff3 = nums[j]-nums[j-1]
                    if diff3 == diff2:
                        count+=1
                    else:
                        break
            
                    
        return count
                

