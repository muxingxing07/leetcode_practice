class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        tree = defaultdict(set)
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        # 分别用记录每个结点子结点的数量和累计距离
        count = [1] * N
        res = [0] * N

        # dfs1后只有0的累计距离是最终的
        def dfs1(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs1(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    # 从父节点往子结点走的时候，子结点子树的结点距离都会减一，
                    # 所以直接减去子树的数量，而除此以外的都可以加一
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)

        dfs1(0, -1)
        dfs2(0, -1)
        return res