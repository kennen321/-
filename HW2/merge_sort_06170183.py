#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
 def merge_sort(self,List):
     
     if 1 >= len(List):
         return List
     
     Mid = round(len(List)/2)
     LList = []
     RList = []
    
     LList =List[0:Mid]
     RList = List[Mid:]
     
     LData = Solution().merge_sort(LList)
     RData = Solution().merge_sort(RList)
     
     return Solution().mergesort(LData, RData)
 def mergesort(self,LList, RList):

    
     if len(LList) == 0: 
         return RList 
     elif len(RList) == 0: 
         return LList 
     
     elif LList[0] < RList[0]:
         return [LList[0]] + Solution().mergesort(LList[1:], RList)
     
     else: 
         return [RList[0]] + Solution().mergesort(LList, RList[1:])

List=[5,3,4,7,2,8,6,1]
Solution().merge_sort(List)

