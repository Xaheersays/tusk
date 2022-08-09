
def heapifydown(arr,i):
  n=len(arr)
  while i < n//2 :
    l,r=(2*i)+1,(2*i)+2
    max_idx=l  if l<n and arr[l] > arr[i] else i
    max_idx=r if r<n and arr[r] > arr[max_idx] else max_idx
    if max_idx==i:
      break
    arr[max_idx],arr[i]=arr[i],arr[max_idx]
    i=max_idx
  

def crateheap(arr):
  for i in range((len(arr)//2)-1,-1,-1):
    heapifydown(arr,i)


arr=[10,2,100,3,6,5,4,7,8,9]
crateheap(arr)
print(arr)


#-->  ans
#-->  [100, 9, 10, 8, 6, 5, 4, 7, 3, 2]
