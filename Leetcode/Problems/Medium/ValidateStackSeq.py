class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        n=len(pushed)
        newStack = []
        while i<n:
            newStack.append(pushed[i])
            while newStack and newStack[-1] == popped[j]:
                newStack.pop()
                j+=1
            i+=1
        return not newStack
        
        
