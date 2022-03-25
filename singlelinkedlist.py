class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
  

class MyLinkedList:
    def __init__(self):
      self.size = 0
      self.head = Node(None)
        
    def get(self, index):
      if index < 0 or index >= self.size:
        return -1
      cur = self.head
      for _ in range(index+1):
        cur = cur.next
      return cur.val
  
    def addAtHead(self, val):
      self.addAtIndex(0, val)
  
    def addAtTail(self, val):
      self.addAtIndex(self.size, val)
  
    def addAtIndex(self, index, val):
      if index > self.size:
        return
      if index < 0:
        index = 0
      self.size += 1
      pre = self.head
      for _ in range(index):
        pre = pre.next
      to_add = Node(val)
      to_add.next = pre.next
      pre.next = to_add
  
    def deleteAtIndex(self, index):
      if index < 0 or index >= self.size:
        return
      self.size -= 1
      pre = self.head
      for _ in range(index):
        pre = pre.next
      pre.next = pre.next.next


linkedList = MyLinkedList()
linkedList.addAtHead(1)
print(linkedList.get(0))

linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)

print(linkedList.get(1))
linkedList.deleteAtIndex(1)
print(linkedList.get(1))