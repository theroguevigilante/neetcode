class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            if s[l]!=s[r]:
                if not s[l].isalnum():
                    l+=1
                    continue
                elif not s[r].isalnum():
                    r-=1
                    continue
                return False
            l+=1
            r-=1
        return True
