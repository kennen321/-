#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
 def get(self,List):
     
     if 1 >= len(List):
         return List
     
     Mid = round(len(List)/2)
     LList = []
     RList = []
    
     LList =List[0:Mid]
     RList = List[Mid:]
     
     LData = Solution().get(LList)
     RData = Solution().get(RList)
     
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
Solution().get(List)

