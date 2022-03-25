class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res=0
        diff = [y-x for x,y in costs ]
        diff.sort()
        n=len(costs)
        for i in range(n//2):
            res+=costs[i][0]+costs[n//2+i][0]+diff[i]
                
        return res
