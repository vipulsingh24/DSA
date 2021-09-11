"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""

def find_majority_element(arr):
    element_freq = {}
    for element in arr:
        element_freq[element] = element_freq.get(element, 0) + 1

    for element in element_freq.keys():
        if element_freq[element] > len(arr) // 2:
            return element

    return None



if __name__ == "__main__":
    arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
    print(find_majority_element(arr))
