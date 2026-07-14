class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        lastdig=n-1
        if n==1:
            if digits[lastdig]==9:
                return [1,0]
            newdig=digits[0]+1
            return [newdig]
        while True:
            if digits[lastdig]>=0 and digits[lastdig]<=8 :
                digits[lastdig]+=1
                return digits

            elif digits[lastdig]==9:
                while(digits[lastdig]==9):
                    digits[lastdig]=0
                    lastdig-=1

                if lastdig == -1:
                    return [1] + digits

                digits[lastdig]+=1
                return digits     