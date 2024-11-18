"""
leetcode problem - 56
reference:
Neetcode. (n.d.). Merge Intervals - Sorting - Leetcode 56. YouTube. https://www.youtube.com/watch?v=44H3cEC2fFM&t=354s 

merge intervals 
medium
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_num = output[-1][1]
            if start <= last_num:
                output[-1][1] = max(last_num, end)
            else:
                output.append([start, end])
        return output

