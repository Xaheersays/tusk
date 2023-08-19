nums = [1,2,4,7,3,5,6,9]
n=len(nums)
ans = [0]*n
st = []
for i in range(n-1,-1,-1):
    el = nums[i]
    while st and st[-1] >= el:
        st.pop()
    if st:
        ans[i]=st[-1]
    else:
        ans[i]=-1
    st.append(el)
print(ans)
