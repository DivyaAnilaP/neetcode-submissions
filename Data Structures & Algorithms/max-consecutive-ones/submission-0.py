class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)):
            count=0
            for j in range(i,len(nums)):
                if nums[j]==1:
                    count+=1
                    maxi=max(maxi,count)
                else:
                    break
        return maxi
