class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
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

