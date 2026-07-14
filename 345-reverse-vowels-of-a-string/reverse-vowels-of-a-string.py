class Solution:
    def reverseVowels(self, s: str) -> str:
        word=list(s)
        start=0
        end=len(word)-1
        vowels='aeiouAEIOU'
        while start<end:
            while start<end and vowels.find(word[start]) == -1:
                start+=1
            while start<end and vowels.find(word[end]) == -1:
                end-=1
            temp=word[start]
            word[start]=word[end]
            word[end]=temp

            start+=1
            end-=1
        return "".join(word)