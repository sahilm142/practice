class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        i=0
        while i<n:
            j = i+1
            while j<n:
                target2 = target-nums[i]-nums[j]
                #Checks 2SUM for range j+1,n-1
                start,end = j+1,n-1
                while start<end:
                    _2Sum = nums[start]+nums[end]
                    if _2Sum == target2:
                        res.add((nums[i],nums[j], nums[start], nums[end]))
                        start+=1
                        end-=1
                    elif _2Sum>target2:
                        end-=1
                    else:
                        start+=1
                j+=1
            i+=1
        return res
