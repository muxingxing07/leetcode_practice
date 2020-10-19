# 重构字符串，用栈遍历字符
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s):
            ret = list()
            for ch in s:
                if ch != '#':
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)

        return build(S) == build(T)


# 双指针
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if S[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
