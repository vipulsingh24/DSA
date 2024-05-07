"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            print(l1.val, l2.val)
            if l1.val < l2.val:
                print("l1 less than l2")
                tail.next = l1
                l1 = l1.next
            else:
                print("l2 greater than l1")
                tail.next = l2
                l2 = l2.next
            print("tail: ", tail.val)
            tail = tail.next

        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next
    

if __name__ == "__main__":
    list_1 = ListNode(1)
    list_1.next = ListNode(2)
    list_1.next.next = ListNode(4)

    list_2 = ListNode(1)
    list_2.next = ListNode(3)
    list_2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(list_1, list_2))