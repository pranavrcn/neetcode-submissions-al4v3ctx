class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = []
        count = 0
        for num in nums:
            if num == 0:
                counts.append(count)
                count = 0
            if num == 1:
                count += 1
        counts.append(count)
        return max(counts)
            