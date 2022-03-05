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


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i=0
        while i<n:
            j=i+1
            while j<n:
                start,end = j+1,n-1
                target2 = target - nums[i] - nums[j]
                while start<end:
                    _2sum = nums[start]+nums[end]
                    if _2sum>target2:
                        end-=1
                    elif _2sum<target2:
                        start+=1
                    else:
                        quad = [nums[i], nums[j], nums[start], nums[end]]
                        res.append(quad)

                        # Duplicates items equal to nums[start]
                        while start<end and nums[start] == quad[2]:
                            start+=1
                        # Ignoring Duplicate item equal to nums[end]
                        while start<end and nums[end] == quad[3]:
                            end-=1
                #Ignoring items equal to nums[j]

                while j+1<n and nums[j+1] == nums[j]:
                    j+=1
                j+=1
            # Ignore duplicate i items:
            while i+1<n and nums[i+1]==nums[i]:
                i+=1
            i+=1

        return res

