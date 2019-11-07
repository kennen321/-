```python
程式碼的部分，真的有先搞懂Merge Sort去做思考，不過還是沒什麼頭緒，

所以有上網找了一些資料來參考，網址都有附上~
```


```python
初始想法:將陣列分割直到只有一個元素。

開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列。

接著利用已經排序好的小筆資料合併成排序好的大筆資料。
```


```python
def get(List):
    
     # 如果List只包含一個值，則直接回傳
     if 1 >= len(List):
         return List
     # 找出中間位置
     Mid = int(round(len(List)/2))
     LList = []
     RList = []
     # 將List分成左右兩邊
     LList =List[0:Mid]
     RList = List[Mid:]
     # 不斷分割，直到List內剩下一個值
     LData = get(LList)
     RData = get(RList)
     # 當無法分割時則開始合併
     return mergesort(LData, RData)
```


```python
def mergesort(LList, RList):


    # 判斷左(右)邊的List，如果只有一邊有值，就可直接回傳
     if len(LList) == 0: 
         return RList 
     elif len(RList) == 0: 
         return LList 
     # 比較兩邊List的第一個值，如果右邊大於左邊，那麼就將左邊的第一個值放入，
        #並將後面的值繼續做合併和排序的工作，直到將所有的值都比較完為止
     elif LList[0] < RList[0]:
         return [LList[0]] + mergesort(LList[1:], RList)
     # 與上一段做的工作相同，方向相反
     else: 
         return [RList[0]] + mergesort(LList, RList[1:])


# 這一段撰寫的是分割的Function
```


```python
# 印出回傳的List
List=[5,3,4,7,2,8,6,1]
print(get(List))
```

    [1, 2, 3, 4, 5, 6, 7, 8]
    


```python
[參考Merge的程式碼](https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python)

[參考Merge的程式碼](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)

[參考Merge的程式碼](https://www.geeksforgeeks.org/python-program-for-merge-sort/)
```
