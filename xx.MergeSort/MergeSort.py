class Solution:
    def mergeSort(self, head: ListNode) -> ListNode:
        if head is None: 
            return None
        if head.next is None:
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
        ptr1 = l1
        ptr2 = l2
        prePtr1 = None
        while ptr1 is not None or ptr2 is not None:
            if l1 is None: return l2
            if l2 is None: return l1
            if ptr1 is None:
                prePtr1.next = ptr2
                ptr2 = ptr2.next
                return l1  
            if ptr2 is None:
                return l1
            if ptr1.val <= ptr2.val:
                prePtr1 = ptr1
                ptr1 = ptr1.next                
            else:
                if prePtr1 is None:
                    l1 = ptr2
                    ptr2 = ptr2.next
                    l1.next = ptr1
                    prePtr1 = l1
                else:
                    prePtr1.next = ptr2
                    ptr2 = ptr2.next
                    prePtr1.next.next = ptr1
                    prePtr1 = prePtr1.next
        return l1

