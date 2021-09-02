"""

"""


def can_jump(nums) -> bool:
    if not nums:
        return False

    last_possible_index = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        print("last_possible_index: ", last_possible_index)
        print("i: ", i, "nums[i]: ", nums[i])
        if nums[i] >= last_possible_index - i:
            last_possible_index = i

    return last_possible_index == 0


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))

    nums = [3, 2, 1, 0, 4]
    print(can_jump(nums))

