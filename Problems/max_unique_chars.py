"""
Maximum Length of a Concatenated String with Unique Characters
"""

def max_length(arr):
    result = [-1]

    max_unique_chars_length(arr, "", 0, result)
    if result[0] != -1:
        return result[0]

    return 0


def max_unique_chars_length(arr, curr_str, index, result):
    print("\nCurrent str: ", curr_str)
    print("Index: ", index)
    print("Result: ", result)
    # base case
    if index == len(arr):
        return

    for index in range(index, len(arr)):
        print("Loop index: ", index)
        concat_str = curr_str + arr[index]
        print("Concat str: ", concat_str)
        if len(set(concat_str)) == len(list(concat_str)):
            print("Len match")
            if len(concat_str) > result[0]:
                result[0] = len(concat_str)

            max_unique_chars_length(arr, concat_str, index + 1, result)


"""
def is_unique_char(s):
    set_ = set()
    for i in s:
        if i in set_:
            return False
        set_.add(i)
    return True

def helper(arr, idx):
    if (idx == len(arr)):
        return [""]

    print("Arr: ", arr)
    print("Idx: ", idx)
    tmp = helper(arr, idx + 1)
    print("Tmp: ", tmp)
    ret = tmp # Copy of tmp
    
    for i in tmp:
        test = i + arr[idx]
        print("Test: ", test)
        if is_unique_char(test):
            ret.append(test)

    return ret

def max_length(arr):
    tmp = helper(arr, 0)
    length = 0
   
    for str_ in tmp:
        length = length if length > len(str_) else  len(str_)

    return length
"""

if __name__ == "__main__":
    s = ["", "ab", "cd", "ab"]
    print(max_length(s))
