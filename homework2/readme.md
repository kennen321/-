#   堆積排序法(Heap Sort) 
  
## Definition(MAX HEAP) 
  
● 堆積的節點只有兩個子節點，從左到右排序下來 

● 在堆積排序還有很重要的一點是，父節點的數一定要比子節點大 

● 最大的數被存放在結構的最上方，即是樹根(root) 

● 樹根一定是最大值，將樹根(最大值)與最後一個節點調換， 

● 將最後一個節點(原樹根)取出，並加入已排序數列 

● 對整棵樹重新調整為最大堆積樹 

● 重複步驟依序可以列出答案



#   合併排序法(Merge Sort)

## Definition

● Merge Sort 的核心觀念是將大筆資料切割成很多資料做排序

● 將陣列分割直到只有一個元素。

● 開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列。

● 接著利用已經排序好的小筆資料合併成排序好的大筆資料。

● 程式碼的部分，真的有先搞懂Merge Sort去做思考，不過還是沒什麼頭緒，

● 所以有上網找了一些資料來參考





#  參考資料
[Heap sort Merge sort比較](https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-%E6%BC%94%E7%AE%97%E6%B3%95%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%95%B4%E7%90%86)

[參考Heap的程式碼](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html#)

[參考Heap的程式碼](https://www.runoob.com/w3cnote/heap-sort.html)

[參考Heap的程式碼](https://github.com/pecu/DSA/blob/master/06_HeapSort/heapSort.py)

[參考Merge的程式碼](https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python)

[參考Merge的程式碼](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)

[參考Merge的程式碼](https://www.geeksforgeeks.org/python-program-for-merge-sort/)
