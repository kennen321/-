```python
我對程式還沒有甚麼概念，但是有先理解Heap Sort的運作方式
不過還是對程式碼的部分沒什麼頭緒,所以有上網找了一些資料來參考。
網址是以下這些:
    https://github.com/pecu/DSA/blob/master/06_HeapSort/heapSort.py
    https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html#
    https://www.runoob.com/w3cnote/heap-sort.html
```


```python
首先先一步步來，建立index
```


```python
def heapify(arr,i):
    left = 2*i+1  
    right = 2*i+2 
    largest = i   
    
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)
```


```python
再來數值交換
```


```python
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
```


```python
最後在寫到heapSort
```


```python
def heapSort(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)
    global arrLen
    arrLen = len(arr)
    
    for i in range(len(arr)-1,0,-1):  
        swap(arr,0,i)  
        arrLen -=1
        heapify(arr, 0)
    return arr
```


```python
設計一下變數
```


```python
arr = [ 10, 8, 7, 4, 6, 3, 5 ]
arrLen = len(arr)
heapSort(arr)
```




    [3, 4, 5, 6, 7, 8, 10]




```python
n = len(arr) 
print () 
for i in range(n): 
	print ("%d" %arr[i]),
```

    
    3
    4
    5
    6
    7
    8
    10
    


```python
以下解釋一下程式碼
```


```python
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
```

    Sorted array is
    3
    4
    5
    6
    7
    8
    10
    


```python
最後在整理成助教要的Solution，其實我就是缺少Solution，所以整個程式碼沒有分數
```


```python
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
```

    
    3
    4
    5
    6
    7
    8
    10
    


```python

```
