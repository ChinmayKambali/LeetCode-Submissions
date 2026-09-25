class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0] * n
        rightsum = [0] * n

        lsum = 0
        rsum = 0

        for i in range(n):
            j = -i - 1

            leftsum[i] = lsum
            rightsum[j] = rsum

            lsum += nums[i]
            rsum += nums[j]

        for i in range(n):
            leftsum[i] = abs(leftsum[i] - rightsum[i])

        return leftsum