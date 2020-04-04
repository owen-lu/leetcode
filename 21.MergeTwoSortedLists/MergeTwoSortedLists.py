class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 is None: return l1
        if l1 is None: return l2
        ptr1 = l1
        ptr2 = lastRound = l2
        prePtr2 = None
        while True:
            if ptr1 is None: break
            while True:
                if ptr1.val <= ptr2.val:    
                    tmp = ptr1.next
                    ptr1.next = ptr2
                    if prePtr2 is None:
                        l2 = ptr1
                        prePtr2 = ptr1
                    else:
                        prePtr2.next = ptr1
                        prePtr2 = ptr1
                    ptr1 = tmp                        
                    lastRound = ptr2
                    break
                else:
                    if ptr2.next is None:
                        ptr2.next = ptr1
                        return l2
                    else:
                        if ptr1.val > ptr2.next.val:
                            prePtr2 = ptr2
                            ptr2 = ptr2.next
                            continue
                        else:
                            tmp = ptr1.next
                            ptr1.next = ptr2.next
                            ptr2.next = ptr1
                            ptr1 = tmp
                            lastRound = ptr2.next.next
                            break
                ptr2 = lastRound    
        return l2
