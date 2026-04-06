class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        reversecleaned = ""
        for c in s:
            if c.isalnum():
                cleaned = cleaned + c.lower()
                reversecleaned = c.lower() + reversecleaned
        return cleaned == reversecleaned

        
        