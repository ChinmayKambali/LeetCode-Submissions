class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums)==1:
        #     return False
        # nums2=[]
        # for i in range(len(nums)):
        #     t=nums[i]
        #     nums[i]=0
        #     if t in nums:
        #         return True
        # return False

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        # for i in nums:
        #     if i in nums[nums.index(i)+1:]:
        #         return True
        # return False

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False