# 448.Find All Numbers Disappeared in an Array { https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array }
# 21ms | Beats 80.21%

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        finalarr = []
        setarr = set(nums)

        for i in range(1,len(nums)+1):
            if i not in setarr:
                finalarr.append(i)
        
        return finalarr

  
