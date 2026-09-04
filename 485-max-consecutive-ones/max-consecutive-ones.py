class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0

        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
            
            if max < count:
                max = count
        
        return max
