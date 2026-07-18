class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        for a,b in zip(s,s[1:]):
            if roman[a]<roman[b]:
                res-=roman[a]
            else:
                res+=roman[a]
        # s1=list(s)
        # for i in range(len(s1)):
        #     if s1[i] in roman:
        #         res+=roman.get(s1[i])
        return res+roman[s[-1]]