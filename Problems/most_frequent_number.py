def most_frequent_number(arr, k):
    numbers_frquency = {}
    for i in range(len(arr)):
        if arr[i] in numbers_frquency:
            numbers_frquency[arr[i]] += 1
        else:
            numbers_frquency[arr[i]] = 1


    result_arr = [0] * len(numbers_frquency)
    j = 0

    for item in numbers_frquency:
         result_arr[j] = [item, numbers_frquency[item]]
         j += 1

    result_arr = sorted(result_arr, key=lambda x: x[0], reverse=True)
    result_arr = sorted(result_arr, key=lambda x: x[1], reverse=True)

    for i in range(k):
        print(result_arr[i][0], end=" ")


if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    n = 8
    k = 2
    most_frequent_number(arr, k)
