"""
No two adjacent character in the string are same
Input: aaabbc
Output: ababac or abacab
"""

import heapq


def rearrange_adjacent_chars_different(s):
    char_counts = {}
    for char in s:
         if char in char_counts:
            char_counts[char] += 1
         else:
            char_counts[char] = 1

    heap = [[-1 * count, char] for char, count in char_counts.items()] # [[-3, a], [-2, b], [-1, c]]
    heapq.heapify(heap)
    
    previous_char = "#"

    result = ""
    while len(heap) > 1:
        current_char_element = heapq.heappop(heap)  # [-3, a] > [-2, b] > [-2, a]
        current_char_count = current_char_element[0]  # -3 > -2 > -2
        current_char = current_char_element[-1]  # a > b > a
        
        if current_char != previous_char:
            result += current_char  # result = a > ab > aba
            current_char_count += 1  # current_char_count = -2 > -1 > -1
            
            if current_char_count < 0:
                heapq.heappush(heap, [current_char_count, current_char])  # heap = [[-2,b], [-1,c], [-2, a]] > heap = [[-1,c], [-2, a], [-1, b]] > heap = [[-1,c], [-1, b], [-1, a]]
            previous_char = current_char
           
        else:
            next_char_element = heapq.heappop(heap)
            next_char_count = next_char_element[0]
            next_char = next_char_element[-1]
 
            result += next_char
            next_char_count += 1
            if next_char_count < 0:
                heapq.heappush(heap, [next_char_count, next_char])

            heapq.heappush(heap, [current_char_count, current_char])

            previous_char = next_char  # previous_char = "a" > "b"
        
    if heap:
        last_char_element = heapq.heappop(heap)
        last_char_count = last_char_element[0]
        last_char = last_char_element[-1]

        if last_char_count < -1:
            return "Not possible"
        
        result += last_char

    return result


if __name__ == "__main__":
    s = "aaabbc"
    print(rearrange_adjacent_chars_different(s))
    s = "aaaabc"
    print(rearrange_adjacent_chars_different(s))













