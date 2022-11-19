import math
def dist(p,q):
    xp,yp = p[0],p[1]
    xq,yq = q[0],q[1]
    return math.sqrt((yq-yp)**2  + (xq-xp)**2)
def polar_angle(p,q):
    xp,yp = p[0],p[1]
    xq,yq = q[0],q[1]
    return math.atan2(yq-yp,xq-xp)

def orient(p,q,r):
    xp,yp = p[0],p[1]
    xq,yq = q[0],q[1]
    xr,yr = r[0],r[1]
    val = (yq - yp)* (xr-xq) - (yr-yq)*(xq-xp)
    if val<=0:      #anticlock we want to left
        return 1
    else:
        return 2    #clock we dont want right
class Solution:
    def outerTrees(self, trees):
        min_ = [1000000,1000000]
        for i in trees:
            if i[1] == min_[1]:
                if i[0] < min_[0]:
                    min_ = i.copy()
            if i[1] < min_[1]:
                min_=i.copy()
        trees.sort(key=lambda p: (polar_angle(min_, p)))
        st=[trees[0],trees[1],trees[2]]

        for i in range(3 , len(trees)):
            while len(st)>1 and orient(st[-2],st[-1],trees[i])!=1:
                st.pop()
            st.append(trees[i])
        print(st)
    
