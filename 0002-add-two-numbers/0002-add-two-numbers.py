# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummyHead = ListNode()
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            soma = digit1 + digit2 + carry
            digit = soma % 10
            carry = soma // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result


# # Teste
# if __name__ == '__main__':
#     # Criação das listas ligadas l1 e l2
#     l1 = ListNode(2)
#     l1.next = ListNode(4)
#     l1.next.next = ListNode(3)
# 
#     l2 = ListNode(5)
#     l2.next = ListNode(6)
#     l2.next.next = ListNode(4)
# 
#     # Criação da solução e obtenção do resultado
#     sol = Solution()
#     resultado = sol.addTwoNumbers(l1, l2)
# 
#     # Impressão do resultado
#     while resultado is not None:
#         print(resultado.val, end=" -> " if resultado.next else "\n")
#         resultado = resultado.next
        