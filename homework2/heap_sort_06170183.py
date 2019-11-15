class Solution(object):
 def heapSort(self,arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        self.heapify(arr,i)
    global arrLen
    arrLen = len(arr)
    
    for i in range(len(arr)-1,0,-1):  
        swap(arr,0,i)  
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
        swap(arr, i, largest)
        self.heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [ 10, 8, 7, 4, 6, 3, 5 ]
arrLen = len(arr)
Solution().heapSort(arr)
n = len(arr) 
print () 
for i in range(n): 
	print ("%d" %arr[i]),
