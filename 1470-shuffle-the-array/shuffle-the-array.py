class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=nums[:n]
        nums2=nums[n:]
        nums=[]
        print(nums)
        for i in range (n):
            nums.append(nums1[i])
            nums.append(nums2[i])
        return nums
