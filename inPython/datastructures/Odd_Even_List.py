"""Odd and Even List"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or if not head.next or if not head.next.next:
            return head
        
        node = head
        even = head.next
        temp = node.next 
        count = 0

        while temp:
            if temp.next:
                node.next = temp.next 
            else: 
                if count%2 == 0:
                    node.next = even
                    temp.next = None
                else:
                    temp.next = even
                    node.next = None
                break
            node = temp
            temp = node.next 
            count += 1
        return head