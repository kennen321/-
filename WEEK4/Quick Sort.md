## Quick Sort

快速排序作法：

選定一個基準值(Pivot)

將比基準值(Pivot)小的數值移到基準值左邊，形成左子串列

將比基準值(Pivot)大的數值移到基準值右邊，形成右子串列

分別對左子串列、右子串列作上述三個步驟 ⇒ 遞迴(Recursive)

直到左子串列或右子串列只剩一個數值或沒有數值

Quick Sort(快速排序法)是一種「把大問題分成小問題處理」的Divide and Conquer方法，

數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」。

接著，將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，

「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。

![image](https://github.com/kennen321/DSA2019/blob/master/homework/Quicksort%E6%B5%81%E7%A8%8B%E5%9C%96.png)




## Insertion Sort
Insertion Sort(插入排序作法)
插入排序法(Insertion Sort)是排序演算法的一種，他是一種簡單容易理解的排序演算法，其概念是利用另一個數列來存放已排序部分，

逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。運算流程如下：

從未排序數列取出一元素。

由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面。

重複以上動作直到未排序數列全部處理完成。

![image](https://github.com/kennen321/DSA2019/blob/master/homework/insertion%20sort.png)













參考資料:

https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort)
http://notepad.yehyeh.net/Content/Algorithm/Sort/Quick/Quick.php
https://emn178.pixnet.net/blog/post/93791164
