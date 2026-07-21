class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # nums.sort()
        nums2=[]
        # for i in range(1,n+1):
        #     if i not in nums:
        #         nums2.append(i)
        # return nums2

        s=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in s:
                nums2.append(i)
        print(s)
        print(n)
        return nums2