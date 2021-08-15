def max_number_of_balloons(text):
    count = [0] * 26

    for i in range(len(text)):
        count[ord(text[i]) - ord('a')] += 1

    print("Count: ", count)
    balloon_count = count[1]  # b
    balloon_count = min(balloon_count, count[0])  # a
    balloon_count = min(balloon_count, count[11] / 2)  # l
    balloon_count = min(balloon_count, count[14] / 2)  # o
    balloon_count = min(balloon_count, count[13])  # n

    return balloon_count


if __name__ == "__main__":
    str_ = "loonxbaloballpooonn"
    print(max_number_of_balloons(str_))
