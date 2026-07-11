class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 
        l = 0
        r = 0
        x = set()
        g = 0
        while r < len(s):
            if s[r] in x:
                x.remove(s[l])
                l += 1
            else:
                x.add(s[r])
                g = max(g, r - l + 1)
                r += 1
        return g
