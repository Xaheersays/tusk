arr=[3,5,7,9,1,2,10]
n=len(arr)
ans=[-1]*n
st=[]
for i in range(n):
    while st!=[]:
        if arr[i] > st[-1]:
            break
        else:
            st.pop()
    if st:
        ans[i]=st[-1]
    else:
        ans[i]=-1
    st.append(arr[i])
print(ans)
