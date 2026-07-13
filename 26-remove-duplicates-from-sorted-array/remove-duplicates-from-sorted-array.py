class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = []

        for i in nums[:]: 
            if i in nums2:
                nums.remove(i)
            else:
                nums2.append(i)

        return len(nums)