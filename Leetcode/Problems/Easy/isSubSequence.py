class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        n = len(s)
        m = len(t)
        if n==0 and (m!=0 or m==0):
            return True
        
        for i in range(m):
            if k>=n:
                break
            
            if s[k] == t[i]:
                k+=1
            
        return k==n
        
