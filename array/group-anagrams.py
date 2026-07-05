class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            y = tuple(sorted(i))
            if y in x:
                x[y].append(i)
            else:
                x[y] = [i]

        res = []
        for i in x.values():
            res.append(i)
        return res
