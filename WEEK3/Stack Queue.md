## Stack Queue

### Stack

堆疊(stack)是先進後出(FILO First In Last Out)的資料結構，意思是，先進去的資料最後出來。

用Stack函式庫實作程式不須知道內部程式如何實作，只要知道如何在Stack中新增與刪除資料。

當我們碰到大量資料的時候，通常都會用陣列來處理，資料結構中處理陣列有兩種較常見的方式：堆疊(stack)與佇列(queue)。

可以使用push( )與pop( )來實現。

隱含在函式的遞迴呼叫，因為遞迴的過程中最後呼叫的函式要優先處理，系統會實作堆疊程式自動處理遞迴呼叫，不須自行撰寫堆疊。

特定問題可能需要使用Stack(堆疊)進行解題，可以自行撰寫Stack程式。

### Queue

佇列(queue)是先進先出(FIFO First In First Out)的資料結構，意思是，先進去的資料先出來。

通常用於讓程式具有排隊功能，依序執行工作，例如：印表機同時間有多個檔案等待列印，在印表機內會有一個Queue(佇列)的功能，

將準備列印的檔案暫存在Queue等待印表機提供列印服務，先送到印表機的檔案先印出來。

可以使用push( )與shift( )來實現。

例如：程式的括弧配對檢查，右大括號配對最接近未使用的左大括號，將左大括號加進Stack(堆疊)中，一遇到右大括號就取出配對。

實作Stack的部分，







參考資料:

https://ithelp.ithome.com.tw/articles/10205260

https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/xian-xing-zi-liao-jie-gou-queue-stack-huolinked-list-yu-you-xian-quan-zhu-lie-priority-queue
