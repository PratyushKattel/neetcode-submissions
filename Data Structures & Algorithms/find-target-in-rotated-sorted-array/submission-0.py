class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = (high + low) // 2

            # print(low , mid , high )
            if nums[mid] == target:
                return mid
            
            if nums [low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else :
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    
                    high = mid - 1
        return -1
