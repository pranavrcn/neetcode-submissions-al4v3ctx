class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countsMap = {}
        for num in nums:
            if countsMap.get(num):
                return True
            else:
                countsMap[num] = 1
        return False
                