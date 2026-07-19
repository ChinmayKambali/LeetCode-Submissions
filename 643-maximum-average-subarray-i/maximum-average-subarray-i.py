class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sum=0
        for i in range(k):
            sum+=nums[i]

        maxavg=sum/k
        for i in range(k,n):
            sum+=nums[i]
            sum-=nums[i-k]

            avg=sum/k
            maxavg=max(maxavg,avg)
        return maxavg