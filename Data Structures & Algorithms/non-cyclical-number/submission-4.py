class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while 1:
            
            sum = self.helper(n)
            if sum == 1:
                return True
            if(sum in seen):
                return False

            seen.add(sum)
            n = sum
      
    def helper(self, n:int) -> int:
        sum=0
        while n > 0:
            digit = n % 10
            sum += int(digit*digit)
            n //= 10
        
        return sum
