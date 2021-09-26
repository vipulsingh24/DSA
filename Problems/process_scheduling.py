# process scheduling

import heapq

def minimumTime(ability, processes):
    # Write your code here
    ability = [-1 * a for a in ability]
    heapq.heapify(ability)
    
    processing_time = 0
    while processes >= 1:
        current_process = heapq.heappop(ability)
        current_process_abs = abs(current_process)
        processes -= current_process_abs
        current_process_abs = math.floor(current_process_abs / 2)
        heapq.heappush(ability, -1 * current_process_abs)
        processing_time += 1
        
    return processing_time


j = [7,10, 9,10, 6,3,9,9,10,10]
ps = 122
print(minimumTime(j, ps))  # 20



j = [2,1,5,3,1]
ps = 17
print(minimumTime(j, ps))  # 9
