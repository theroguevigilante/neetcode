class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            temp = str(len(i)) + "*" + i
            res += temp
        return(res)

    def decode(self, s: str) -> List[str]:
        strs, i = [], 0
        while i < len(s):
            n = ""
            while s[i]!="*":
                n+=s[i]
                i+=1
            n = int(n)
            strs.append(s[i+1:i+1+n])
            i = i + 1 + n
        return strs
