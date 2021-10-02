"""
Check if it possible to partition in k subarrays with equal sum
"""

def partition_k_sub_array(arr, k):
    """
    Time and space: O(n)
    """
    n = len(arr)
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]

    for i in range(1, n, 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    # return false if total_sum is not divisible by K
    total_sum = prefix_sum[n-1]
    if total_sum % k != 0:
        return False

    # a temporary variable to check there are exactly K partitions
    count = 0
    pos = -1

    for i in range(0, n, 1):
        if pos == -1:
            sub_sum = 0
        else:
            sub_sum = prefix_sum[pos]

        if prefix_sum[i] - sub_sum == total_sum / k:
            pos = i
            count += 1
        elif prefix_sum[i] - prefix_sum[pos] > total_sum / k:
            break

    return count == k


def partition_k_sub_array_2(arr, k):
    """
    Time: O(n) and space: O(1)
    """
    n = len(arr)
    total_sum = 0
    
    for i in range(n):
        total_sum += arr[i]

    if (total_sum % k != 0):
        return False

    total_sum = total_sum // k
    k_sub_arr_sum = 0
    count = 0

    for i in range(n):
        k_sub_arr_sum += arr[i]
        
        if k_sub_arr_sum == total_sum:
            k_sub_arr_sum = 0
            count += 1

    if count == k:
        return True
    return False

if __name__ == "__main__":
     arr = [4, 4, 3, 5, 6, 2]
     K = 3
     print(partition_k_sub_array(arr, K))
     arr = [4, 4, 3, 5, 6, 2]
     K = 3
     print(partition_k_sub_array_2(arr, K))
