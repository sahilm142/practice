class Solution:
    #do full counting or hashset and check whether it already exists
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute Force: Do the counting
        cnt = Counter(nums)
        return sum(k for k,v in cnt.items() if v>=2)


        
        
