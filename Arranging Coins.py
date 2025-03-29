# 441. Arranging Coins { https://leetcode.com/problems/arranging-coins/submissions/1590302897/ }
# Runtime 5ms | Beats 50.99%

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            total = (mid * (mid + 1)) // 2 
            
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right 
