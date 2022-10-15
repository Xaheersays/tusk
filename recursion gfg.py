# https://www.geeksforgeeks.org/sum-triangle-from-array/

arr = [1, 2, 3, 4, 5]

def Newfun(newArr,arr,i):
    if i >= len(newArr):
        return newArr
    newArr[i] = arr[i]+arr[i+1]
    return Newfun(newArr,arr,i+1)
    
def tri(arr):
    if len(arr) == 1: return 
    newArr = [0]*(len(arr)-1)
    Newfun(newArr,arr,0)
    tri(newArr)
    print(newArr)
    
tri(arr)
print(arr)
