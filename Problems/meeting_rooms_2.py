"""
Find minimum number of meeting rooms required
"""

import heapq

def min_number_of_meeting_rooms(intervals):
    if not intervals:
        return 0

    # sort intervals by start time
    intervals.sort(key=lambda interval: interval[0])

    # Min Heap
    meeting_rooms = [intervals[0][1]]
    heapq.heapify(meeting_rooms)

    for interval in intervals[1:]:
        if interval[0] >= meeting_rooms[0]:
             heapq.heappop(meeting_rooms)
        heapq.heappush(meeting_rooms, interval[1])


    return len(meeting_rooms)



if __name__ == "__main__":
    intervals = [[0,30], [15,20], [5,10]]
    print(min_number_of_meeting_rooms(intervals))
