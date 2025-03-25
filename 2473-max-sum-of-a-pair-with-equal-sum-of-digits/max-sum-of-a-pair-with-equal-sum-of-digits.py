class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = {}
        max_value = -1

        for num in nums:
            digit_sum = sum(map(int, str(num)))
            if digit_sum in hashmap:
                max_value = max(max_value,hashmap[digit_sum]+num)
                hashmap[digit_sum] = max(hashmap[digit_sum],num)
            else:
                hashmap[digit_sum] = num
        
        return max_value


        