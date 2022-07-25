class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        newnode.next = cur.next
        cur.next = newnode
    def addAtBegin(self, val):
        newnode = Node(val)
        cur = self.head
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            return
        while cur.next != self.head:
            cur = cur.next
        cur.next = newnode
        newnode.next = self.head
        self.head = newnode
    def addAfter(self, nodegiven, val):
        newnode = Node(val)
        cur = self.head
        newnode.next = nodegiven.next
        nodegiven.next = newnode
    def createCircularLinkedList(self, list_node):
        for node in list_node:
            self.append(node)
    def removeNode(self, val):
        cur = self.head
        if self.head is None:
            return
        if self.head.val == val and self.head.next == self.head:
            self.head = None
            return
        if self.head.val == val:
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
            return
        while cur.next != self.head:
            if cur.val == val:
                break
            prev = cur
            cur = cur.next
        if cur == self.head:
            return
        prev.next = cur.next

    def printCLinkedList(self):
        cur = self.head
        if self.head is None:
            print("None")
            return
        while cur:
            print(cur.val, end="->")
            cur = cur.next
            if cur == self.head:
                break
        print("None")
    def getLength(self):
        cur = self.head
        count = 0
        if cur is None:
            return count
        while True:
            count += 1
            if cur.next == self.head:
                return count
            cur = cur.next


def checkCircularLinkedList(llist):
    cur = llist.head
    if llist.head is None:
        return True
    cur = cur.next
    while cur != llist.head:
        if cur is None:
            return False
        cur = cur.next
    return True
