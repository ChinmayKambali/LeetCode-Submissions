class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        sum = count = 0

        for n in nums:
            sum += n
            target=sum-k
            if target in sub_num:
                count += sub_num[target]
            
            sub_num[sum] = 1 + sub_num.get(sum, 0)
        
        return count