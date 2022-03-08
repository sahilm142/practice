class Solution:
    def maxLen(self, n, arr):
        #Code here
        #Brute Force
        maxx = 0 
        for i in range(n):
            sm = 0
            for j in range(i,n):
                sm+=arr[j]
                if sm==0:
                    maxx = max(maxx, j-i+1)
        return maxx

class Solution:
    def maxLen(self, n, arr):
        #Code here
        #Using Hashmap to store prefix sum
        #if SUM[i:j] = X and SUM[i:k] = X where j<k
        #SUM[i:j] = SUM[i:k] = SUM[i:j]+SUM[j:k]
        #implies SUM[j:k] == 0
        #TC: O(N)
        maxx = 0 
        sm = 0
        hm = {}
        for i in range(n):
            sm += arr[i]
            if sm==0:
                maxx = i+1
            else:
                if sm in hm:
                    maxx = max(maxx, i-hm[sm])
                else:
                    hm[sm] = i
        return maxx
