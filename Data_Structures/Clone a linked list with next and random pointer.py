class Solution:
    #Function to clone a linked list
    def copyList(self, head):
        oldToCopy = {None : None}
        
        cur = head
        while cur:
            copy = Node(cur.data)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.arb = oldToCopy[cur.arb]
            cur = cur.next
            
            
        return oldToCopy[head]
