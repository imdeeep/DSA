
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newintervals = []

        for intv in intervals:
            if not newintervals or newintervals[-1][1] < intv[0]:
                newintervals.append(intv)
            else:
                newintervals[-1][1] = max(newintervals[-1][1], intv[1])

        return newintervals