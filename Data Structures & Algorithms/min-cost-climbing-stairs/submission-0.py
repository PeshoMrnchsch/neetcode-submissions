class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(n, cache:list[int]):
            nonlocal cost
            if n == 0:
                cache[0] = cost[n]
                return cache[0]
            
            if n==1:
                cache[1] = cost[n]
                return cache[1]
            
            if cache[n] != -1:
                return cache[n]
            
            cache[n] = cost[n] + min(dfs(n-1, cache), dfs(n-2, cache))
            return cache[n]

        cache = [-1]*len(cost)
        return min(dfs(len(cost)-1, cache), dfs(len(cost)-2, cache))