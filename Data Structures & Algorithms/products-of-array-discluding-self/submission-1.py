class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_pre = [1 for _ in range(len(nums))]
        post = 1
        for i in range(1, len(nums)):
            nums_pre[i] = nums_pre[i - 1] * nums[i - 1]
        print(nums_pre)

        for j in range(len(nums) - 1, -1, -1):
            nums_pre[j] *= post
            post *= nums[j]

        return nums_pre
