class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class Solution(object):
 def insert(self,root,val):
    if root is None:
        root = val
        return root
    else:
        if root.value > val.value:
            if root.left is None:
                root.left = val
                return root.left
            else:
                Solution().insert(root.left,val)
        else:
            if root.right is None:
                root.right = val
                return root.right
            else:
                Solution().insert(root.right,val)

 def in_order_print(self,root):
    if not root:
        return
    Solution().in_order_print(root.left)
    print (root.value)
    Solution().in_order_print(root.right)

 def pre_order_print(self,root):
    if not root:
        return        
    print (root.value)
    Solution().pre_order_print(root.left)
    Solution().pre_order_print(root.right)

 def post_order_print(self,root):
    if not root:
        return        
    Solution().post_order_print(root.left)
    Solution().post_order_print(root.right)
    print (root.value)
 
 def search(self,root,target): 
        if target == root.val:
            return root
        elif target > root.val:
            if root.right == None:
                return False
            else:
                return Solution().search(root.right,target)
        elif target < root.val :
            if root.left == None:
                return False
            else:
                return Solution().search(root.left,target)

def delete(self,root,target):
    if root is None:
        root = target
        return root
    else:
        if root.value > target.value:
            if root.left is None:
                root.left = target
                return root.left
            else:
                Solution().delete(root.left,target)
        else:
            if root.right is None:
                root.right = target
                return root.right
            else:
                Solution().delete(root.right,target)

        if root.left is None:
                    target = root.right
                    root = None
                    return target

        elif root.right is None:
                    target = root.left
                    root = None
                    return target




        

