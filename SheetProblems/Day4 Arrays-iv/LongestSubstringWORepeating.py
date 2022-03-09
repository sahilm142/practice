class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        #sliding window, add items to hashmap 
        #add element with their index in seen if it's already there and outside 
        #our current window no issue else increase the starting point to 1+last index where it was present
        #keep updating maxLength found so far
        start_ind,end_ind = 0,0
        n=len(s)
        seen = {}#set(s[start_ind:end_ind])
        while end_ind<n:
            if s[end_ind] not in seen:
                maxLength = max(maxLength, end_ind-start_ind+1)
            else:
                if seen[s[end_ind]]< start_ind:
                    maxLength = max(maxLength, end_ind-start_ind+1)
                else:
                    start_ind = seen[s[end_ind]]+1
            seen[s[end_ind]] = end_ind
            end_ind+=1
        return maxLength
