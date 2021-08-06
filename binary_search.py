# Binary Search Algo


def binary_search(data, item):
    max_idx = len(data) - 1
    lower_idx = 0
    upper_idx = max_idx

    while lower_idx <= upper_idx:
        mid_point = (lower_idx + upper_idx) // 2
        print("Mid Point: ", mid_point)
        
        if data[mid_point] == item:
           return mid_point

        if item > data[mid_point]:
            lower_idx = mid_point + 1
        else:
            upper_idx = mid_point - 1

    if lower_idx > upper_idx:
        return None

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
print(binary_search(items, 41))
