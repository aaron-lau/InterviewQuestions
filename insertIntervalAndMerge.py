# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        return result

# s = Solution()
# solution1 = s.insert([Interval(1,3),Interval(6,9)], Interval(2,5))
# solution2 = s.insert([Interval(1,5),Interval(7,15),Interval(20,25)], Interval(5,10))
# solution3 = s.insert([Interval(5,10),Interval(15,20),Interval(25,35)], Interval(7,17))
