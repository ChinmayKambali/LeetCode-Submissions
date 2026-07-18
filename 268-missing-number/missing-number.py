class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(10000):
            if i not in nums:
                return i