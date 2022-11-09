arr=[100,80,60,70,60,75,85]
n=len(arr)
ans=[0]*n
st=[]
i=n-1
while i>-1:
    if st==[]:
        ans[i]=-1
        st.append(arr[i])
    elif st!=[] and st[-1] > arr[i]:
        ans[i] = st[-1]
        st.append(arr[i])
    elif st!=[] and st[-1] <= arr[i]:
        while st and not st[-1]>arr[i]:
            st.pop()
        if st==[]:
            ans[i] =-1
        else:
            ans[i]=st[-1]
            st.append(arr[i])
    i-=1
print(ans)
