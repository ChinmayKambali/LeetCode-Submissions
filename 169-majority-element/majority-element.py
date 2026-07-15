class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=Counter(nums)
        n=len(set(nums))
        maxi=0
        for i in set(nums):
            temp=counts[i]
            if temp > maxi:
                maxi = temp
                result = i
        return result