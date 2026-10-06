class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(keys:list[int], n : int):
            if keys[n] != -1:
                return keys[n]

            if n == 1:
                keys[n] = 1
                return 1
            if n == 2: 
                keys[n] = 2
                return 2
            
            keys[n] = helper(keys, n-1) + helper(keys, n-2) 
            return keys[n]
            
        keys = [-1]*(n+1)
        return helper(keys, n)
            