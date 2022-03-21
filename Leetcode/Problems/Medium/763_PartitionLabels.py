class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        #get the last index of each unique char in s
        last_ind = {}
        for i in range(len(s)):
            last_ind[s[i]] = i
            
        start=0
        while start<len(s):
            end = last_ind[s[start]]
            #print(start,end)
            partition = s[start:end]
            j=0
            while j<len(partition):
                if end<last_ind[partition[j]]:
                    end = last_ind[partition[j]]
                    partition = s[start:end]
                j+=1
            #if partitions are needed just add these partition to res  
            res.append(len(partition)+1)
            start+=len(partition)+1
            

        return res

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        #get the last index of each unique char in s
        last_ind = {}
        for i in range(len(s)):
            last_ind[s[i]] = i
            
        start=0
        while start<len(s):
            end = last_ind[s[start]]
            #print(start,end)
            j=start+1
            while j<end:
                if end < last_ind[s[j]]:
                    end = last_ind[s[j]]
                j+=1
                    
            res.append(end-start+1)
            start = end+1
            

        return res
        
        
