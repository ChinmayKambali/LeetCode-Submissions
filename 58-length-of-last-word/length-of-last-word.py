class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        n=len(s)-1
        count=0
        for i in s[n]:
            count+=1
        return count