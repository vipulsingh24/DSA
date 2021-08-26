"""
find maximum contiguous subarray
"""

def max_sub_array_sum(arr):
    n = len(arr)
    max_so_far = -9999
    max_ending_here = 0

    for i in range(n):
        print("\nmax_ending_here: ", max_ending_here) #
        max_ending_here += arr[i] # 0+-2,-2, 0 _3, -3
        print("max_ending_here 2: ", max_ending_here) # -2,-3, 
        print("max_so_far: ", max_so_far)  # -9999,0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here  # -2
        print("max_so_far 2: ", max_so_far)

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

if __name__ == "__main__":
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sub_array_sum(a))
