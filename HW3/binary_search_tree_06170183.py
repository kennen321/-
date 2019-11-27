class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def Print_BT(self): 
        if self.left:
            self.left.PrintBT()
        print(self.val)
        if self.right:
            self.right.PrintBT()
        
class Solution(object):
 def insert(self,root,val):
    if root is  None:
        root = TreeNode(val)
        return root
        
    else:
        if root.val >= val:
            if root.left is None:
                root.left = TreeNode(val)
                return root.left
            else:
                root=root.left
                return(Solution().insert(root,val))
        else:
            if root.right is None:
                root.right = TreeNode(val)
                return root.right
            else:
                root=root.right
                return(Solution().insert(root,val))

 
 
 def search(self,root,target):
        if root is None:
            return 
        elif target == root.val:
            return root
        elif target > root.val:
            root=root.right
            return Solution().search(root,target)
        elif target < root.val :
            root=root.left
            return (Solution().search(root,target))

 def delete(self, root, target):
        a = Solution().search(root,target)
        while a is not None: 
        
            if root is None: 
                return root
        
            if root.val > target : 
                root.left = Solution().delete(root.left,target) 
        
            elif  root.val < target : 
                root.right = Solution().delete(root.right,target)
            else: #當找到值的時候
                if root.left is None : #如果左邊是None
                    temp = root.right 
                    root = None #刪掉root值
                    return temp #回傳temp值
            
                if root.right is None :
                    temp = root.left
                    root = None
                    return temp
        
                change = Solution().SmallNode(root.right) 
                root.val = change.val 
                root.right = Solution().delete(root.right,change.val) 
            a = Solution().search(root,target)
        return root
 
 def delete(self,root,target):
    temp=Solution().search(root,target)
    while temp is not None:
     if root is None:
        return root
     else:
        if root.val > target:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            else:
                root.left=Solution().delete(root.left,target)
        else:
            if root.right is None:
                temp=root.left
                root=None
                return temp
            else:
                root.right=Solution().delete(root.right,target)
                
            exchange = Solution().SNode(root.right) 
            root.val = exchange.val 
            root.right = Solution().delete(root.right,exchange.val) 
        temp = Solution().search(root,target)
     return root
                
 def SNode(self,root): 
        
        minv = root
        if minv.left is not None: 
            minv = minv.left
            return(Solution().SNode(minv))
        return minv       

     
 def modify(self, root, target, nval):
        count = 0 
        temp = Solution().search(root,target) 
        while temp is not None and temp.nval == target: 
            count += 1
            temp = temp.left 
            
        Solution().delete(root,target)
        
        for i in range(count):
            Solution().insert(root,nval)
        return root
