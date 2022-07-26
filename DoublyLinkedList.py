class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
       self.head = None
    def printDoublyLinkedList(self):
        cur = self.head
        if self.head is None:
            print("None")
            return
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("None")
    def printReverseDoublyLinkedList(self):
        cur = self.head
        if cur is None:
            print("None")
            return
        while cur.next:
            cur = cur.next
        while cur:
            print(cur.val, end="<-")
            cur = cur.prev
        print("None")
    def append(self, val):
        cur = self.head
        newnode = Node(val)
        if cur is None:
            self.head = newnode
            return
        while cur.next:
            cur = cur.next
        cur.next = newnode
        newnode.prev = cur
    def addAtBegin(self, val):
        newnode = Node(val)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
        self.head = newnode
    def addAfter(self, nodegiven, val):
        newnode = Node(val)
        if newnode is None:
            return
        newnode.next = nodegiven.next
        if nodegiven.next is not None:
            nodegiven.next.prev = newnode
        nodegiven.next = newnode
        newnode.prev = nodegiven
    def addBefore(self, nodegiven, val):
        newnode = Node(val)
        if nodegiven is None:
            return
        newnode.prev = nodegiven.prev
        if nodegiven.prev is None:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            return
        nodegiven.prev.next = newnode
        newnode.next = nodegiven
        nodegiven.prev = newnode
    def removeNode(self, val):
        cur = self.head

        if cur and cur.val == val:
            self.head = cur.next
            self.head.prev = None
            return
        while cur:
            cur = cur.next
            if cur.val == val:
                break
        cur.prev.next = cur.next
        if cur.next is not None:
            cur.next.prev = cur.prev
    def createDoublyLinkedList(self, list_node):
        for node in list_node:
            self.append(node)


