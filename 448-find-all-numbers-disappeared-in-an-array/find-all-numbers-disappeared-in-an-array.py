class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        n=len(nums)
        nums2=[]
        for i in range(1,n+1):
            if i not in s:
                nums2.append(i)
        return nums2