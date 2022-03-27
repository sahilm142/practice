class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {}
        for i in range(len(mat)):
            res[i] = 0
            for j in range(len(mat[0])):
                if mat[i][j]!=0:
                    res[i]+=1
                else:
                    break
        
        out = [k for k,v in sorted(res.items(), key = lambda item:item[1])]
        return out[:k]
        
