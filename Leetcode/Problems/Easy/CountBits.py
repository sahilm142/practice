class Solution:
    def countOnes(self, num):
        cnt = 0
        while num:
            num = num&(num-1)
            cnt+=1
        return cnt
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countOnes(i))
        return res

#Recursion
class Solution:
    def count(self, num):
        if num==0 or num==1:
            return num
        if num%2==0:
            return self.count(num//2)
        else:
            return 1+self.count(num//2)
    
    def countBits(self, n: int) -> List[int]:
        #Brute Force: Traverse through list till n and count ones 
        #Optimized1: Recursion
        #0->0, 1->1, Odd -> 1+Count(Num/2), Even -> Count(Num/2)
        
        res = []
        for i in range(n+1):
            res.append(self.count(i))
            
        return res

#Add Memoization+Recursion
class Solution:
    def count(self, num, memo):
        if num==0 or num==1:
            return num
        if memo[num]:
            return memo[num]
        if num%2==0:
            memo[num] = self.count(num//2, memo)
            return memo[num]
        else:
            memo[num] = 1+self.count(num//2,memo)
            return memo[num]

    def countBits(self, n: int) -> List[int]:
        #Brute Force: Traverse through list till n and count ones
        #Optimized1: Recursion
        #0->0, 1->1, Odd -> 1+Count(Num/2), Even -> Count(Num/2)

        res = [0 for _ in range(n+1)]
        for i in range(n+1):
            res[i] = self.count(i, res)

        return res

#Bottom UP DP, Store the prv calculated val, Count(N even) = Count(N//2), Count(N odd) = Count(N-1)
class Solution:

    def countBits(self, n: int) -> List[int]:
        #Brute Force: Traverse through list till n and count ones
        #Optimized1: Recursion
        #0->0, 1->1, Odd -> 1+Count(Num/2), Even -> Count(Num/2)

        #Bottom UP DP
        res = [0 for _ in range(n+1)]
        for i in range(n+1):
            if i%2==0:
                res[i] = res[i//2]
            else:
                res[i] = 1+res[i-1]

        return res
