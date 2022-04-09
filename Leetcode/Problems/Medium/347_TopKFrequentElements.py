#Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).items()
        
        n = len(nums)
        
        buckt = [[] for _ in range(n+1)]
        
        for num, freq in cnt:
            buckt[freq].append(num)
        
        res = []
        
        for i in range(len(buckt)-1, -1, -1):
            for j in range(len(buckt[i])):
                res.append(buckt[i][j])
        
        return res[:k]
        
#Counting and sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt = sorted(cnt, key=cnt.get, reverse=True)
        return cnt[:k]
