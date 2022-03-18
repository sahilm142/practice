class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        lookup_ind = {}
        
        for i in range(len(s)):
            lookup_ind[s[i]] = i
            
        res = []
        seen = set()        
        
        for i in range(len(s)):
            #if it's already added to final result keep going
            if s[i] in seen:
                continue
            
            #else check if the previous element can be removed (if greater than current element) and added later again using lookup_ind for that element
            while res and res[-1]>s[i] and lookup_ind[res[-1]]>i:
                seen.remove(res[-1])
                res.pop()
            res.append(s[i])
            seen.add(s[i])
            
        
        #print(res)
        
        return ''.join(res)
        
