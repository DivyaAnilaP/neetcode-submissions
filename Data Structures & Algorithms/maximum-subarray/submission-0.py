class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        curr_sum=0
        for num in nums:
            curr_sum+=num
            if curr_sum>maxi:
                maxi=curr_sum
            if curr_sum<0:
                curr_sum=0
        return maxi