"""
Given a string s, return the minimum number of characters you need to delete to make s good.
"""

def min_char_delete(s):
    n = len(s)
    char_map = {}
    for i in range(n):
        char_map[s[i]] = char_map.get(s[i], 0) + 1

    priority_queue = [char_freq for _, char_freq in char_map.items()]
    priority_queue = sorted(priority_queue) # [1,1,3,3]
    char_count = 0

    while (len(priority_queue) > 0):
        frequent = priority_queue[-1]  # 3, 3, 2, 1, 1
        del priority_queue[-1]  # [1,1,3], [1,1,2], [1,1], [1], []

        # if only one char / element in list
        if len(priority_queue) == 0:
            return char_count # 2

        if frequent == priority_queue[-1]:  # 3==3, 3==2, 2==1. 1==1
            if frequent > 1:  # 3 > 1-True, 1 > 1-False
                priority_queue.append(frequent - 1)  # [1,1,3,2]

            char_count += 1  # 1, 2

        priority_queue = sorted(priority_queue)  # [1,1,2,3], [1,1,2], [1,1], [1]

    return char_count

       
if __name__ == '__main__':
    s = "abbbcccd"     
    print(min_char_delete(s))
