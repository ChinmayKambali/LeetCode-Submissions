class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        total=0
        for i in nums:
            total+=i
        leftsum=0
        for i in range(n):
            rightsum=total-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1