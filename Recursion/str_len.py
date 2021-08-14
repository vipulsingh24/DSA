def str_len(a):
    if a == "":
        return 0

    return 1 + str_len(a[1:])
