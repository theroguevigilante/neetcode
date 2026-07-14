# First non idiomatic solve
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        window  = defaultdict(int)
        for i in range(l, r+1):
            if i < len(s2):
                window[s2[i]]+=1
        mainmap = defaultdict(int)
        for i in s1:
            mainmap[i]+=1
        while r < len(s2):
            if window == mainmap:
                return True
            window[s2[l]]-=1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l+=1
            r+=1
            if r < len(s2):
                window [s2[r]]+=1
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mainmap = defaultdict(int)
        for i in s1:
            mainmap[i]+=1
        
        window = defaultdict(int)
        for i in range(len(s1)):
            window[s2[i]]+=1

        if window == mainmap:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r]]+=1
            window[s2[r - len(s1)]]-=1
            if window[s2[r - len(s1)]] == 0:
                del window[s2[r - len(s1)]]
            if window == mainmap:
                return True
        return False
