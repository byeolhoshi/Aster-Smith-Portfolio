"""
Sort a linked list using insertion sort.
"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None: 
            return None
        
        sort = head #create a sort linked list equal to the head listnode
        head = head.next #move the head node over
        sort.next = None #set the sort node's next pointer = to None
        
        while head != None: #while the value of head is not None
            current = head #create a current node and set it equal to head
            head = head.next #move the head node over
            if current.val < sort.val: #if the current node's value is less than the sort node's,
                current.next = sort #   make the current node point to the sort value, 
                sort = current #        then set the sort node to the current node
            else: #otherwise
                search = sort # create a new node called search and make it equal to sort
                while search.next != None and current.val > search.next.val: 
                    #while search is pointing at a valid arg and current's val is greater than
                    #that next value
                    search = search.next #increment the search
                current.next = search.next #set current's next pointer to search's next pointer
                search.next = current #make search's next pointer current
        return sort
       
       
          
        """"
        while current_node is not None: 
            if current_node.val > next_node.val:
                x = current_node.val
                current_node.val = next_node.val
                next_node.val = x
        """
            
        
        
        
