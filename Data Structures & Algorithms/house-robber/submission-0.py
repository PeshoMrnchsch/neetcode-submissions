class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(n, cache):

            nonlocal nums
            if n < 0:
                return 0
            if cache[n] != -1:
                return cache[n]
            
            cur = max(nums[n] + dfs(n-2, cache), dfs(n-1,cache))
            cache[n] = cur
            return cur

        n = len(nums)
        cache = [-1] * n
        return dfs(n-1,cache)