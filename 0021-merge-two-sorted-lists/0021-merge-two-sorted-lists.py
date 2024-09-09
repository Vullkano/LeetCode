# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            
            if not list2:
                return None
            
            else:
                return list2
        else:
            
            if not list2:
                return list1
            
            else:
                dummyHead = ListNode()
                tail = dummyHead
                
                while list1 or list2:
                    
                    if list1 is None:
                        digit1 = float('inf')
                    else:
                        digit1 = list1.val
                    

                    if list2 is None:
                        digit2 = float('inf')
                    else:
                        digit2 = list2.val


                    if digit1 < digit2:
                        newNode = ListNode(digit1)
                        list1 = list1.next
                    else:
                        newNode = ListNode(digit2)
                        list2 = list2.next

                    tail.next = newNode
                    tail = tail.next
                
                return dummyHead.next