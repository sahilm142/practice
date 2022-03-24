class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        start,end=0, len(people)-1
        while start<=end:
            if people[start]+people[end]<=limit:
                end-=1
                start+=1
            elif people[end]<=limit:
                end-=1
            else:
                start+=1
            res+=1
                
        return res
