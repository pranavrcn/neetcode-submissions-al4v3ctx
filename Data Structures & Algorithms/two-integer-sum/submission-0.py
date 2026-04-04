class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                j = prevMap[n]
                return [j, i]
            diff = target - n
            prevMap[diff] = i
        return
