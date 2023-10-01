# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val_1 = (l1.val if l1 else 0)
            val_2 = (l2.val if l2 else 0)
            carry, out = divmod(val_1 + val_2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


if __name__ == "__main__":
    l1 = [ListNode(2), ListNode(4),ListNode(3)]
    l2 = [ListNode(5), ListNode(6), ListNode(4)]
    print(Solution().addTwoNumbers(l1, l2))