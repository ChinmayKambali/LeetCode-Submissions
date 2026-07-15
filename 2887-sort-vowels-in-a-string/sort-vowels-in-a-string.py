class Solution:
    def sortVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        s1=[]
        for i in s:
            if i in vowels:
                s1.append(i)
        s1.sort()
        ans=list(s)
        j = 0
        for i in range(len(ans)):
            if ans[i] in vowels:
                ans[i]=s1[j]
                j+=1

        return "".join(ans)