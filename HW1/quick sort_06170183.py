def quick_sort(list): 
    little = []
    large = []
    middle = [] #建立三個空的list，用來放置元素

    if len(list) <= 1:
        return list  #當list裡的元素數量<=1，直接回傳list，不須再進行大小比較

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                little.append(i)
            elif i > key: #比key值大的數
                large.append(i)
            else:
                middle.append(i)

   little = quick_sort(little)
    large = quick_sort(large)
    return little + middle + large
