
# https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/

nums   = [1, 4, 3, -5, -4, 8, 6]

#   first approach 01
# consvertion for loop into recursive function
def Solve(nums,MinEle,MaxEle):
    n = len(nums)
    def Find(nums,i):
        nonlocal MinEle , MaxEle ,n
        if i == n : return 
        ans = nums[i:i+1]
        MinEle = min(MinEle , ans[0])
        MaxEle = max(MaxEle , ans[0] )
        return Find(nums,i+1)
    Find(nums,0)
    return MinEle,MaxEle
print(Solve(nums,9,-1))


# second approach 02

# a) for min

def solve(nums,n):
    if n == 1:
        return nums[0]
    return min(nums[n],solve(nums,n-1))
print(solve(nums,len(nums)-1))


# b) for max 


def solve1(nums,n):
    if n == 1:
        return nums[0]
    return max(nums[n],solve1(nums,n-1))
print(solve1(nums,len(nums)-1))