def heapify(arr,i):
    left = 2*i+1  #父節點中i的左子節點位置
    right = 2*i+2 #父節點中i的右子節點位置
    largest = i   #將i值設給變數largest
    #如果左子節點大於父節點 把左節點設為新的父節點
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    #如果右子節點大於父節點 把右節點設為新的父節點
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    #如果父節點有更動 就把兩兩交換
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)
#數值交換
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)
    global arrLen
    arrLen = len(arr)
    
    for i in range(len(arr)-1,0,-1):  #從最後一個數開始一個一個跑到陣列的第2個位置
        swap(arr,0,i)  #呼叫函式將數值交換
        arrLen -=1
        heapify(arr, 0)
    return arr



arr = [ 10, 8, 7, 4, 6, 3, 5 ]#用剛才 heapify 過的結果來測試：成功完成
arrLen = len(arr)
heapSort(arr)

n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
	print ("%d" %arr[i]),
