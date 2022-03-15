class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        cnt=0
        st=[]
        
        for i in range(len(s)):
            if s[i] == '(':
                cnt+=1
                st.append(i)
            elif s[i] == ')':
                if cnt>0:
                    cnt-=1
                    st.pop()
                else:
                    st.append(i)
                    
        while len(st)!=0:
            s[st.pop()]=''
            
        return ''.join(s)
        
