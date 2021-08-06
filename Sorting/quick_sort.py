# Quick Sort Algorithm


def quick_sort(data, start, end):
    print(" Quick Sort Data: {}, start: {}, end: {}".format(data, start, end))
    if start < end:
        pivot_idx = partition(data, start, end)  # [6, 20, 19, 8] 0, 3 -> 
        print("Pivot idx: ", pivot_idx)
    
        quick_sort(data, start, pivot_idx-1)
        print("Completed first quick sort call, data: ", data)
        quick_sort(data, pivot_idx+1, end)
    return data

def partition(data, start, end):
    print(" Partition Data: {}, start: {}, end: {}".format(data, start, end))
    pivot_value = data[start]  # 6
    lower = start + 1  # 1
    upper = end  # 3

    done = False
    while not done:
        while lower <= upper and data[lower] <= pivot_value:
            print("Lower decre: ", lower)
            lower += 1
 
        while upper >= lower and data[upper] >= pivot_value:  # 3 (pass), 2 (pass), 1 (pass)
            print("Upper decre: ", upper)
            upper -= 1  # 2, 1, 0
            print("Upper decre after: ", upper)

        if upper < lower:
            done = True
        else:
            temp = data[lower]
            data[lower] = data[upper]
            data[upper] = temp

    temp = data[start]
    data[start] = data[upper]
    data[upper] = temp

    return upper


if __name__ == "__main__":
    # items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    items = [6, 20, 19, 8]
    print(items)
    print(quick_sort(items, 0, len(items) - 1))
