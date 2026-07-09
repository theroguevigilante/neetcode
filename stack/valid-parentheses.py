class Solution:
    def isValid(self, s: str) -> bool:
        m = { ')': '(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in m and stack and stack[-1]==m[c]:
                stack.pop()
                if stack and stack[-1]==m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
