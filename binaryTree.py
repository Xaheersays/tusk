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


d=Node("d")
e=Node("e")
f=Node("f")
g=Node("g")
c=Node("c",f,g)
b=Node("b",d,e)
a=Node("a",b,c)




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





