class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_count = {0:1}
        sum = 0
        count = 0

        for n in nums:
            sum += n
            remainder = sum % k

            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = 1 + remainder_count.get(remainder, 0)
        
        return count