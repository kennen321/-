class Solution(object):
 def heap_sort(self,arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        self.heapify(arr,i)
    global arrLen
    arrLen = len(arr)
    
    for i in range(len(arr)-1,0,-1):  
        
        arr[i], arr[0] = arr[0], arr[i]
        arrLen -=1
        self.heapify(arr, 0)
    return arr

 def heapify(self,arr,i):
    left = 2*i+1  
    right = 2*i+2 
    largest = i   
    
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        self.heapify(arr, largest)


arr = [ 9, 3, 0, 0, 42, 1, -1,3,22,-50,42,-1 ]
arrLen = len(arr)
Solution().heap_sort(arr)
n = len(arr)
print(arr)

