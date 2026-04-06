class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []
        pairs = {")":"(", "}":"{", "]":"["}
        opening = ["(", "{", "["]
        if not s[0] in opening:
            return False
        for c in s:
            if c in opening:
                pStack.append(c)
            elif len(pStack) != 0:
                opened = pStack.pop()
                if opened != pairs.get(c):
                    return False
            elif c:
                return False
        if len(pStack) == 0:
            return True
        return False
