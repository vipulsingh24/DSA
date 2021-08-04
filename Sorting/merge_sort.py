# Merge Sort Algorithm


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        print("mid: ", mid)
        left_arr = data[:mid]
        right_arr = data[mid:]
        print("Left array: ", left_arr)
        print("Right array: ", right_arr)
        
        merge_sort(left_arr)
        merge_sort(right_arr)

        print("Left array after: ", left_arr)
        print("Right array after: ", right_arr)


        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
               data[k] = left_arr[i]
               i += 1
            else: 
               data[k] = right_arr[j]
               j += 1
            k += 1

        # If the left array still has the values
        while i < len(left_arr):
            data[k] = left_arr[i]
            i += 1
            k += 1

        # If the right array still has the values
        while j < len(right_arr):
            data[k] = right_arr[j]
            j += 1
            k += 1

    return data


if __name__ == "__main__":
    # items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    items = [6, 20, 19, 8]
    print(items)
    print(merge_sort(items))
