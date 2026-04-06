class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            midpoint = (l + r) // 2
            if target > nums[midpoint]:
                l = midpoint + 1
            elif target < nums[midpoint]:
                r = midpoint - 1
            elif target == nums[midpoint]:
                return midpoint
        return -1
