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


a=Node("a",Node("b",Node("d"),Node("e")),Node("c",Node("f"),Node("g")))


a.data
<<<'a'
a.left.data
<<<'b'
a.right.data
<<<'c'
a.left.left.data
<<<'d'
left
a.left.right.data
<<<'e'
a.right.data
<<<'c'
a.right.left.data
<<<'f'
a.right.right.data
<<<'g'




def inorder(root):
    if root :
        inorder(root.left)
        print(root.data)
        inorder(root.right)
inorder(a)        

# ans<<<    
def inorder(root):
    if root :
        inorder(root.left)
        print(root.data)
        inorder(root.right)
inorder(a)        
d
b
e
a
f
c
g


inorder(a)        
def inorder(root):
    if root :
        inorder(root.left)
        print(root.data)
        inorder(root.right)
inorder(a)   
#ans<<<

d
b
e
a
f
c
g


def postorder(root):
    if root :
        preorder(root.left)
        preorder(root.right)
        print(root.data)
        
preorder(a)
#ans<<<

a
b
d
e
c
f
g

