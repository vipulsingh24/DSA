"""
Partition array into N subsets with balanced sum
"""

import heapq

def balanced_sum(arr, partition):
    heap = [(0, i) for i in range(partition)]
    res = [[] for _ in range(partition)]

    for num in sorted(arr, reverse=True):
        print("\nheap: ", heap)
        print("res: ", res)
        val, idx = heapq.heappop(heap)
        print("Value: ", val, "Idx: ", idx)
        total = val + num
        res[idx].append(num)

        print("Heap: ", heap)
        heapq.heappush(heap, (total, idx))

    return res


if __name__ == "__main__":
    a =  [1, 2, 3, 4, 5]
    print(balanced_sum(a, 3))
