# 难
# 回溯法+set集合
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos = set()
        neg = set()
        res = 0

        def backtrack(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if j not in col and i - j not in pos and i + j not in neg:
                    col.add(j)
                    pos.add(i - j)
                    neg.add(i + j)
                    backtrack(i + 1)
                    col.remove(j)
                    pos.remove(i - j)
                    neg.remove(i + j)

        backtrack(0)
        return res
