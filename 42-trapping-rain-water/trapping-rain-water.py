class Solution:
    def trap(self, height: list[int]) -> int:
        lwall=rwall=0
        n=len(height)
        lmax=[0]*n
        rmax=[0]*n
        sum=0
        
        for i in range(n):
            j= -i-1
            lmax[i]=lwall
            rmax[j]=rwall
            lwall=max(lwall,height[i])
            rwall=max(rwall,height[j])
        print(lmax)
        print(rmax)
        
        for i in range(n):
            potential=min(lmax[i],rmax[i])
            sum+=max(0,potential-height[i])
        
        return sum