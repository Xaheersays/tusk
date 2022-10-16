#https://www.geeksforgeeks.org/sum-triangle-from-array/
#python code

nums = [1,2,3,4,5]

def make_new_Arr(newArr,nums,i):
    if i < len(newArr):
        newArr[i] = nums[i]+nums[i+1]
        make_new_Arr(newArr,nums,i+1)
    return

def Array(nums):
    n = len(nums)
    if n ==1 : return
    newArr = [0]*(n-1)
    make_new_Arr(newArr,nums,0)
    Array(newArr)
    print(newArr)

Array(nums)
print(nums)

