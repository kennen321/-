from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def NMD5(self,key):
        target=MD5.new()
        target.update(key.encode('utf-8'))
        lock=target.hexdigest()
        return int(lock,16)
        
    



    def add(self, key):
        global number
        global look
        number=self.NMD5(key)
        look=number % self.capacity
        if self.data[look] is not None:
            x=self.data[look]
            if x.next is not None:
                x=x.next
            x.next=ListNode(count)

       
    def remove(self, key):
        if self.contains(key)==True and self.data[look].val==number:
            self.data[look]=self.data[look].next
        else:
            top=self.data[look]
            while top.next != count:
                top=top.next
            top.next=top.next.next
        if self.contains(key):
            self.remove(key)
        return
    def contains(self, key):
         if self.data[look] is not None:
            top =self.data[look]
            while top.val != count:
                top=top.next
            if top is None:
                return False
            else:
                return True
