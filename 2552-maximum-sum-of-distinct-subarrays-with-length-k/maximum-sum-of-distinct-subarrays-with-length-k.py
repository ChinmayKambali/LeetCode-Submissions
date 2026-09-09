class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        windowsum = 0
        n = len(nums)
        freq = {}

        # First window
        for i in range(k):
            windowsum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        maxsum = 0

        if len(freq) == k:
            maxsum = windowsum

        # Slide the window
        for i in range(k, n):

            # Add new element
            windowsum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # Remove old element
            windowsum -= nums[i-k]
            freq[nums[i-k]] -= 1

            # If frequency becomes 0, remove it
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]

            # All k elements are unique
            if len(freq) == k:
                maxsum = max(maxsum, windowsum)

        return maxsum