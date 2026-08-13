"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Array of tuples
        # Determine if overlap
        # maintain busy tuple'
        if not intervals:
            return True
        intervals.sort(key=lambda interval: interval.start)
        start_range = intervals[0].start
        end_range = intervals[0].end
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < end_range:
                return False
            # it's okay to set end_range unconditionally
            # even if there is a gap between end_range
            # and start, as, given that we sorted by start,
            # we know for a fact that nothing later will
            # want to fill that gap
            end_range = end
        return True
