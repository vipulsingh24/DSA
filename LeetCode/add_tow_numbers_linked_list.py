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
    list_1 = ListNode(2)
    list_1.next = ListNode(4)
    list_1.next.next = ListNode(3)

    list_2 = ListNode(5)
    list_2.next = ListNode(6)
    list_2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(list_1, list_2))