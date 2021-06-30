# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        if len(intervals) == 0 :
            return [new_interval]
        
        answer = []
        
        num_intervals = len(intervals)
        i = 0
        while i < num_intervals and intervals[i].end < new_interval.start :
            i += 1
        answer.extend(intervals[:i])
        if i == 0 and new_interval.end < intervals[i].start :
            answer.append(new_interval)
            answer.extend(intervals)
            return answer
        if i < num_intervals :
            temp_interval = Interval()
            temp_interval.start = min(intervals[i].start, new_interval.start)

            while i < num_intervals and intervals[i].start <= new_interval.end :
                i += 1
            temp_interval.end = max(new_interval.end, intervals[i-1].end)

            answer.append(temp_interval)
        
            if i < num_intervals :
                answer.extend(intervals[i:])
        else :
            answer.append(new_interval)
    
        return answer
