"""
find maximum contiguous subarray
"""

def max_sub_array_sum(arr):
    n = len(arr)
    max_so_far = -9999
    max_ending_here = 0

    for i in range(n):
        print("\nmax_ending_here: ", max_ending_here)
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

"""
         -99999                     0
no.     max_so_far                max_ending_here
-2    -9999 < -2 = -2            0 + -2 = -2 => 0
-3    -2 < -3 = -2               0 + -3 = -3 => 0
4      -2 < 4 = 4                0 + 4 = 4
-1     4 < 3 = 4                 4 + -1 = 3
-2     4 < 1 = 4                 3 + -2 = 1
1      4 < 2 = 4                 1 + 1 = 2
5      4 < 7 = 7                 2 + 5 = 7        
-3     7 < 4 = 7                 7 + -3 = 4
"""
