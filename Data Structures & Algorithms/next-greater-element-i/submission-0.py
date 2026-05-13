class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nge={}
        for num in nums2:
            while stack and stack[-1]<num:
                smaller=stack.pop()
                nge[smaller]=num
            stack.append(num)

        while stack:
            nge[stack.pop()]=-1

        ans=[]
        for num in nums1:
            ans.append(nge[num])
        return ans
