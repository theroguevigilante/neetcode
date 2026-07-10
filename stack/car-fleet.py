class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        d = []
        for i, p in enumerate(position):
            d.append([p, speed[i]])
        d.sort()
        d.reverse()
        stack = [(target - d[0][0]) / d[0][1]]
        for p, s in d[1:]:
            t1 = (target - p) / s
            t2 = stack[-1]
            if t1 > t2:
                stack.append(t1)
        return len(stack)
