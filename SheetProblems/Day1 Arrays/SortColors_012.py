#Simple Brute Force just sort the array and return
#Count the no's of 0's 1's and 2's and update the array
#Optimized
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 0
        low=0
        high = len(nums)-1

        #shifting all 0's to the beginning
        #all 2's to the end
        #use two pointer two track and swap to move them to correct position

        while mid<=high and mid>=low:
            if nums[mid]==0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1



