class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        

        
a=Node("a")
b=Node("b")
c=Node("c")

a.left=b
a.right=c
print(a.data)
print(a.left.data)
print(a.right.data)
