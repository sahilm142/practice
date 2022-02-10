#Brute Force: O(n^3)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute Force: 2^n?
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i,n):
                sm = sum(nums[i:j+1])
                if sm == k:
                    cnt+=1
        return cnt
                
#O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute Force: 2^n -> TLE
        #Create one array to store sum
        # add all elements in arr and remove the current i later and proceed
        # TLE
        #Create 1-d array to store element's sum
        # from index i -> j and use that to calculate further

        n = len(nums)
        cnt = 0
        sm = [0 for _ in range(n)]
        sm[0] = nums[0]
        #Store sum for 0-i in sm[0][i]
        for i in range(1,n):
            sm[i] = nums[i]+sm[i-1]

        cnt+=sm.count(k)
        ## Now Sum[i,j] == Sum[0,j]-Sum[0,i]
        for i in range(n):
            for j in range(i+1,n):
                target = sm[j]-sm[i]
                if target==k:
                    cnt+=1
        #print(sm)
        return cnt

#Using HashMap and storing sum freq
#O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute Force: O(n^3) -> TLE
        #Create one array to store sum
        # add all elements in arr and remove the current i later and proceed
        # TLE
        #Create 1-d array to store element's sum
        # from index i -> j and use that to calculate further
        #TLE O(n^2)
        #Current One : O(n)

        n = len(nums)
        cnt = 0
        sm = 0#[0 for _ in range(n)]
        hs = {0:1}
        #Store sum for 0-i in sm[0][i]
        for i in range(n):
            sm += nums[i]
            cnt+=hs.get(sm-k, 0)
            hs[sm] = hs.get(sm,0)+1

        #print(sm)
        return cnt


