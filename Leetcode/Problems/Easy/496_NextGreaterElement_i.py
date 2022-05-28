class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        res = [-1]*n1
        for i in range(n1):
            if nums1[i] in nums2:
                ind = nums2.index(nums1[i])
                for k in range(ind+1, len(nums2)):
                    if nums2[k]>nums1[i]:
                        res[i] = nums2[k]
                        break
        
        return res
        
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        st = []
        
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
                
            while st and st[-1] <= num:
                st.pop()
            
            hm[num] = st[-1] if st else -1

            st.append(num)
        
        return [hm[num] for num in nums1]
