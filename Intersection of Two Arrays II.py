# 350.Intersection of Two Arrays II { https://leetcode.com/problems/intersection-of-two-arrays-ii/description/y }
# Runtime 11ms | Beats 17.06%

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)

        return result
