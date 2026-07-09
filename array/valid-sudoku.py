class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rr = defaultdict(set)
        cc = defaultdict(set)
        ss = defaultdict(set)
        for r in range(0, 9):
            for c in range(0, 9):
                element = board[r][c]
                if element == ".":
                    continue
                elif ( element in rr[r] or element in cc[c] or element in ss[r//3, c//3]):
                    return False
                rr[r].add(element)
                cc[c].add(element)
                ss[r//3, c//3].add(element)
        return True
