class Solution:
    def isPalindrome(self, s):
        return s==s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                skip_right = s[left:right]
                skip_left = s[left+1:right+1]
                return self.isPalindrome(skip_right) or self.isPalindrome(skip_left)
            left,right=left+1, right-1
                
        return True                
                
