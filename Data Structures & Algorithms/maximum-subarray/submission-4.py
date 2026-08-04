class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums [0]
        curr_sum = nums [ 0 ]
        #start with max sum being 0th eleement
        for num in nums[1:]:
            curr_sum = max (0 ,curr_sum ) # if curr_sum become -ve make it zero , cause we always start from there 
            curr_sum += num
            # print(curr_sum)
            max_sum = max ( max_sum, curr_sum)

        return max_sum