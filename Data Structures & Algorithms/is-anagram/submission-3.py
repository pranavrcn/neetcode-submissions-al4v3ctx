class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap1 = {}
        countMap2 = {}
        for c in s:
            if countMap1.get(c):
                countMap1[c] += 1
            else: countMap1[c] = 1
        for c in t:
            if countMap2.get(c):
                countMap2[c] += 1
            else: countMap2[c] = 1
        return countMap1 == countMap2