class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a']*n
        k-=n
        while k>0:
            val = k
            if k>=25:
                val = 25
            res[n-1] = chr( 97 + val)
            k -= val
            n -= 1
                
        return ''.join(res)

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        for i in range(n, 0, -1):
            val = k-(i-1)
            #print(val)
            if val>=26:
                res.append('z')
                k-=26
            else:
                res.append(chr(val +ord('a')-1))
                k-=val

        return ''.join(res)[::-1]

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a']*n
        #print(res)
        k-=n
        while k>0:
            #print(chr(ord(res[n-1])+min(25,k)))
            res[n-1] = chr(ord(res[n-1])+min(25,k))
            k-=min(25,k)
            n-=1
                
        return ''.join(res)
