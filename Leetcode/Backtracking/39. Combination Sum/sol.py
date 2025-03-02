class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            # 两个Base cases
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # 左子树：继续包括当前元素
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # 右子树：不继续包括当前元素
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
