class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0:
            return "" 
        tMap = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            tMap[c] += 1
        res = [-1,-1]
        rSize = float("INF")
        l, r = 0, 0
        target = len(tMap)
        curr = 0
        for r in range(len(s)):
            window[s[r]]+=1
            if s[r] in tMap and tMap[s[r]] == window[s[r]]:
                curr+=1
            while curr == target:
                if (r - l + 1) < rSize:
                    res = [l, r]
                    rSize = r - l + 1
                window[s[l]]-=1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    curr -= 1
                l+=1
        l, r = res
        return s[l: r+1] if rSize != float("INF") else ""
