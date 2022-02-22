class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st = []
        n = len(intervals)
        if n==0:
            return st
        #sort the array based on first value (start time)
        intervals.sort(key = lambda x:x[0])
        #create one stack to store the values of the intervals
        st = [intervals[0]]
        
        for i in range(1, n):
            # take top element from stack
            # if endtime of top element is greater than start time of 
            # current interval update endtime of current element with
            # max of curr endtime and curr interval's endtime
            if st[-1][1] >= intervals[i][0]:
                st[-1][1] = max(intervals[i][1], st[-1][1])
            else:
                st.append(intervals[i])
        return st
            
        
