class Solution:
    def modBinarySearch(self, nums, low, high, target):
        mid = low + (high - low)//2
        if low<=high:
            if nums[mid] == target:
                return True
            
            while low < mid and nums[low] == nums[mid]:
                low+=1
            
            if nums[low] <= nums[mid]:
                if nums[mid]>=target and nums[low]<=target:
                    return self.modBinarySearch(nums, low, mid-1, target)
                else:
                    return self.modBinarySearch(nums, mid+1, high, target)
            else:
                if nums[mid]<=target and nums[high]>=target:
                    return self.modBinarySearch(nums, mid+1, high, target)
                else:
                    return self.modBinarySearch(nums, low, mid-1, target)
        else:
            return False
        
    def search(self, nums: List[int], target: int) -> bool:
        #Brute linear search
        return self.modBinarySearch(nums, 0, len(nums)-1, target)        
