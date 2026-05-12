class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        left,right=0,len(nums)-1
        pos=len(nums)-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res[pos]=nums[left]*nums[left]
                left+=1
            else:
                res[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return res
