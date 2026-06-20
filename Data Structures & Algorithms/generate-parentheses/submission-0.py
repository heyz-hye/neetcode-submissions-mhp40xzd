class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n < 1:
            return res

        def dfs(subset, open_count, close_count):
            if len(subset) == 2 * n:
                res.append(''.join(subset))
                return
            if open_count < n:
                subset.append('(')
                dfs(subset, open_count + 1, close_count)
                subset.pop()
            if close_count < open_count:
                subset.append(')')
                dfs(subset, open_count, close_count + 1)
                subset.pop()

        dfs([], 0, 0)
        return res