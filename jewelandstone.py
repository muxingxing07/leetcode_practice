class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
