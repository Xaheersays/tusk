ans=None
def f(root,low,high):
    if root is None :
        return 0
    if root.val <=high and root.val>=low:
        global ans
        ans+=root.val
    f(root.left,low,high)
    f(root.right,low,high)


def solve(root, low, high):
    global ans
    ans=0
    
    f(root,low,high)
    return ans
###############################################
def solve(root, low, high):
    sum_=0
    def f(root):
        if root:
            if root.val > low :
                f(root.left)
            if root.val >=low and root.val<= high :
                nonlocal sum_
                sum_+=root.val
            if root.val <high:
                f(root.right)
    f(root)
    return sum_
  ###############################################
  class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        def f(root):
            if root:
                f(root.left)
                if low <= root.val and high >= root.val:
                    self.ans += root.val
                f(root.right)
        f(root)
        return self.ans
