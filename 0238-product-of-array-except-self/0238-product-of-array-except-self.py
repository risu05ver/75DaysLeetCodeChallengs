class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Step 1: Left product (prefix)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Right product (suffix)
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer