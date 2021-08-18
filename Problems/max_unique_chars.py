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


if __name__ == "__main__":
    s = ["", "ab", "cd", "ab"]
    print(max_length(s))
