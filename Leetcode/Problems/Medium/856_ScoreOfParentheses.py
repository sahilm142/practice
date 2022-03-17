class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        st = []
        for i in range(len(s)):
            if s[i]=='(':
                st.append(score)
                score=0
            elif st:
                curr = st.pop()
                score += curr + max(score, 1)
        return score
