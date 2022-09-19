###Find position of an element in a sorted array of infinite numbers
##### https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
##o(logN)
class InfiniteArray(object):
    
    def findRange(self,array,target):
        s=0
        e=1
        ##block of size 2

        ##if target element is > end then we double the size
        try:
            while target > array[e]:
                temp=e+1
                e=e+((e-s+1)*2) ##double the size of the box
                s=temp
            ##now we have the range in which it lies
            return self.binarySearch(array,target,s,e)

        except:
            pass
            # ("end out of bound")
            
    def binarySearch(self, arr, target, start,end):
        while start <= end:
            mid=(start+end)//2
            if target < arr[mid]:
                end=mid-1
            elif target > arr[mid]:
                start=mid+1
            else:
                ##match
                return mid
        
        return -1

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
find=100
obj1 = InfiniteArray()
ans=obj1.findRange(arr,find)
if ans == -1:
    print ("Element not found")
else:
    print ("Element found at index",ans)
