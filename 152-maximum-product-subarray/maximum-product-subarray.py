class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = minPro = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxPro ,minPro = minPro,maxPro

            maxPro = max(num, maxPro * num)
            minPro = min(num, minPro * num)

            result = max(result, maxPro)
        
        return result
