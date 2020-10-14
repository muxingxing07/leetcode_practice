class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        minfreq = [float('inf')] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1   #ord函数返回字符对应得ASCII数值
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return reduce(lambda x, y: x&y, map(Counter, A)).elements()

