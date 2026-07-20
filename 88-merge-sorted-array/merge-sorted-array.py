class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count=1
        nums2_counter=0
        for i in range(m,m+n):
            if nums1[i]==0:
                nums1[i]=nums2[nums2_counter]
                nums2_counter+=1
        nums1.sort()