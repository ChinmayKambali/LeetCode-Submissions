class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=nums[0]
        currsum=0
        for i in nums:
            currsum+=i
            maxsum=max(currsum,maxsum)

            if currsum<0:
                currsum=0
        return maxsum