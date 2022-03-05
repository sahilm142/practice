class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
        return [-1,-1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = set()
        for i in range(len(nums)):
            if (target-nums[i]) in val:
                return [i, nums.index(target-nums[i])]
            else:
                val.add(nums[i])
                
        return [-1,-1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i,n in enumerate(nums):
            if (target-n) in val:
                return [i, val[target-n]]
            else:
                val[n] = i


        return [-1,-1]

