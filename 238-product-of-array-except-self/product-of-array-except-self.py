class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lmult=1
        rmult=1
        n=len(nums)
        l=[0]*n
        r=[0]*n
        for i in range(n):
            j=-i-1
            l[i]=lmult
            r[j]=rmult
            lmult*=nums[i]
            rmult*=nums[j]
        return [i*j for i,j in zip(l,r)]
                