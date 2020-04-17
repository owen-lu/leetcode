class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        endOfSortedList = dummyHead
        pre = None
        while head is not None:
            if pre is None or (pre.val != head.val):
                endOfSortedList.next = head
                endOfSortedList = endOfSortedList.next
                pre = endOfSortedList
            else:
                pre = head
            head = head.next
        endOfSortedList.next = None
        return dummyHead.next
