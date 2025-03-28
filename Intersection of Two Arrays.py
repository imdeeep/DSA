# 349. Intersection of Two Arrays { https://leetcode.com/problems/intersection-of-two-arrays/description/ }
# Runtime 0ms | Beats 100.00%


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1.intersection(nums2))

        
  
