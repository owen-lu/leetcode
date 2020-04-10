    def mergeSort(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.getMiddleAndSplit(head)
        leftPart = self.mergeSort(head)
        rightPart = self.mergeSort(mid)
        return self.mergeTwoLists(leftPart, rightPart)
    
    def getMiddleAndSplit(self, head: ListNode) -> ListNode:
        pre = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow
         
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        endOfSortedList = dummyHead
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                endOfSortedList.next = l1
                l1 = l1.next                
            else:
                endOfSortedList.next = l2
                l2 = l2.next
            endOfSortedList = endOfSortedList.next 
        if l1 is not None:
            endOfSortedList.next = l1
        if l2 is not None:
            endOfSortedList.next = l2                   
        return dummyHead.next

