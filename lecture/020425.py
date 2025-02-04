'''

def findNum(num, intList):
    if len(intList) == 0:
        return False
    if num == intList[0]:
        return True
    return findNum(num, intList[1:])


assert findNum(1, []) == False
assert findNum(3, [1,2,3]) == True
assert findNum(1, [3,4,5,6]) == False
assert findNum(2, [3,2,1]) == True

'''

'''

LINEAR DATA STRUCTURES 

elements are next to each other (relative positioning)

QUEUE

first in, first out
enqueue, dequeue

DEQUE 

is a linear data structure that is more flexicble than a stack or queue
also known as a "double-ended queue"
a queue allows us to insert and remove from both ends

'''


class Stack:    #last in, first out

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]



def test_InsertIntoStack():
    s = Stack()
    s.push("there")
    s.push("hi")
    assert s.size() == 2
    assert s.peek() == "hi"
    assert s.isEmpty() == False

def test_DeleteFromStack():
    s = Stack()
    s.push("there")
    s.push("hi")
    x = s.pop()
    assert x == "hi"
    assert s.peek() == "there"
    assert s.size() == 1
    assert s.isEmpty() == False
    y = s.pop()
    assert y == "there"
    assert s.size() == 0
    assert s.isEmpty() == True



class Queue:    #first in, first out

    def __init__(self):
        self.line = []

    def isEmpty(self):
        return self.line == []

    def size(self):
        return len(self.line)

    def enqueue(self, item):
        self.line.insert(0, item)

    def dequeue(self):
        return self.line.pop()

def test_InsertIntoQueue():
    q = Queue()
    assert q.isEmpty() == True
    assert q.size() == 0
    q.enqueue("customer1")
    q.enqueue("customer2")
    assert q.isEmpty() == False
    assert q.size() == 2

def test_RemoveFromQueue():
    q = Queue()
    assert q.isEmpty() == True
    q.enqueue("customer1")
    q.enqueue("customer2")
    assert q.dequeue() == "customer1"
    assert q.isEmpty() == False
    assert q.size() == 1
    assert q.dequeue() == "customer2"
    assert q.isEmpty() == True
    assert q.size() == 0



class Deque:    #double-ended queue, both LIFO and FIFO

    def __init__(self):
        self.deck = []

    def isEmpty(self):
        return self.deck == []

    def size(self):
        return len(self.deck)

    def addRear(self, item):
        self.deck.insert(0, item)

    def addFront(self, item):
        self.deck.append(item)

    def removeRear(self):
        return self.deck.pop(0)

    def removeFront(self):
        return self.deck.pop()

def test_Deque():
    d = Deque()
    assert d.isEmpty() == True
    assert d.size() == 0
    d.addFront(10)
    d.addFront(20)
    d.addRear(30)
    d.addRear(40)
    assert d.isEmpty() == False
    assert d.size() == 4
    assert d.removeFront() == 20
    assert d.removeRear() == 40
    assert d.removeRear() == 30
    assert d.removeFront() == 10
    assert d.isEmpty() == True
    assert d.size() == 0