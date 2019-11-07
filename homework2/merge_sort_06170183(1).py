#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


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


# In[3]:


# 印出回傳的List
List=[9,8,7,6,5]
print(get(List))

