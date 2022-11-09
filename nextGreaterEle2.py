arr=[100,80,60,70,60,75,85]
n=len(arr)
ans=[0]*n
st=[]
for i in range(n-1,-1,-1):
    while st!=[]:
        if st[-1]>arr[i]:
            break
        else:
            st.pop()
    if st:
        ans[i]=st[-1]
    else:
        ans[i]=-1
    st.append(arr[i])
print(ans)
