class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
    def __str__(self):
        return f"{self.data}-->{self.next}"

def printll(head):
    while head:
        print(head.data)
        head=head.next

def countll(head):
    count=0
    while head:
        count+=1
        head=head.next
    print(f"there are {count} nodes")
    
def insert_at_last(head,data):
    while head.next:
        head=head.next
    head.next=Node(data)

def insert_at_front(head,data):
    return Node(data,head)
    
def delete_node(head,k):
    ptr=1
    while head:
        head=head.next
        ptr+=1
        if ptr==k-1:
            head.next=head.next.next
            break


a=Node(1,Node(2,Node(3,Node(4))))
str(a)
printll(a)
