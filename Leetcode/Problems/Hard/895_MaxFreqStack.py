class FreqStack:

    def __init__(self):
        self.st = []
        self.hm = {}
        

    def push(self, val: int) -> None:
        
        #Add freq of val in hm
        if val in self.hm:
            self.hm[val] += 1
        else:
            self.hm[val] = 1
        
        #if len of stak freq < current val freq -> append empty stack to store freq stack with val
        if len(self.st)<self.hm[val]:
            self.st.append([])
            
        #Append val to correct freq stack
        self.st[self.hm[val]-1].append(val)

    def pop(self) -> int:
        #Get the last element added to max frequency stack
        frq_element = self.st[-1].pop()
        
        #Check if there is no item in last stack, remove empty stack
        if not self.st[-1]:
            self.st.pop()
            
        #Update the freq for current popped element
        self.hm[frq_element]-=1
        return frq_element
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
