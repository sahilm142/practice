class Solution:
    def binarySearch(self, nums, low, high, target):
        mid = low + (high-low)//2
        
        if low<=high:
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                return self.binarySearch(nums, low, mid-1, target)
            else:
                return self.binarySearch(nums, mid+1, high, target)
        else:
            return -1
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
