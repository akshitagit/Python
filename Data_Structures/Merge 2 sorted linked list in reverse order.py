def mergeResult(h1,h2):
    #return head of merged list
    num1=[]
    num2=[]
    t1=h1
    t2=h2
    while t1:
        num1.append(t1.data)
        t1=t1.next
    while t2:
        num2.append(t2.data)
        t2=t2.next
    num3=num1+num2
    num3.sort()
    num3=num3[::-1]
    num3
    r=Llist()
    tail=None
    for i in num3:
        tail=r.insert(i,tail)
    return r.head

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        resHead=mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
