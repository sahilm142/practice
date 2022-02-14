
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #FInd the largest index such that nums[i]<nums[i+1]
        largest_ind = -1
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                largest_ind = i

        if largest_ind == -1:
            nums.reverse()
        else:

            #find the largest index li such that nums[lrgest_ind]<nums[li]
            #and li>lrgest_ind
            for i in range(largest_ind+1, n):
                if nums[largest_ind]<nums[i]:
                    li = i

            #print(largest_ind,li)
            #Swap these two elements
            nums[largest_ind], nums[li] = nums[li], nums[largest_ind]
            #Reverse the part from Largest_ind+1:
            nums[largest_ind+1:] = reversed(nums[largest_ind+1:])


