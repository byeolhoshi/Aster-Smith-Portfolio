""" 
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        headlist = []
        current_node = head
        while current_node is not None: 
            #print(current_node.val)
            headlist.append(current_node.val)
            current_node = current_node.next 
       
        #print(headlist)
        decimal = 0 
        n = len(headlist)
        headlist.reverse()
        for i in range(n): 
            
            if headlist[i] == 1: 
                x = headlist[i]
                print(x, i)
                decimal+= (x*(2**i))
            else: 
                pass
        
        return decimal
