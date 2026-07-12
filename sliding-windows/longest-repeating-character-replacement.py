class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       x = defaultdict(int)
       c = 0
       l = 0
       for r in range(len(s)):
           x[s[r]] += 1
           while (r - l + 1) - max(x.values()) > k:
               x[s[l]]-=1
               l+=1
           c = max(c, r - l + 1)
       return c
