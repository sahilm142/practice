class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt_top = Counter(tops)
        cnt_bottom = Counter(bottoms)
        
        n=len(tops)
        
        max_top,max_top_freq = cnt_top.most_common(1)[0]
        max_bottom,max_bottom_freq = cnt_bottom.most_common(1)[0]
        
        cnt1, cnt2,res=0,0,-1
        
        for i in range(n):
            if tops[i]==max_top or bottoms[i]==max_top:
                cnt1+=1
            if tops[i]==max_bottom or bottoms[i]==max_bottom:
                cnt2+=1
        #print(cnt1, max_top_freq, cnt2, max_bottom_freq, n, flg)
        
        res1,res2 = cnt1-max_top_freq, cnt2-max_bottom_freq
        
        if cnt1==n and cnt2==n:
            res = min(res1, res2)
        elif cnt1==n:
            res = res1
        elif cnt2==n:
            res=res2
            
        
        return res

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt_top = Counter(tops)
        cnt_bottom = Counter(bottoms)
        
        n=len(tops)
        same = Counter()
        
        for top, bottom in zip(tops, bottoms):
            if top==bottom:
                same[top]+=1
        
        for i in range(1,7):
            if cnt_top[i] + cnt_bottom[i] - same[i] == n:
                return min(cnt_top[i], cnt_bottom[i])-same[i]
        
        return -1
