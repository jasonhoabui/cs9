from LinkedList import LinkedList, Node

def test_NodeCreation():
    n = Node(20)
    assert n.getData() == 20
    assert n.getNext() == None

def test_NodeSetData():
    n = Node(20)
    n.setData(200)
    assert n.getData() == 200

def test_NodeSetNext():
    n = Node(20)
    n2 = Node(10)
    n.setNext(n2)
    assert n.getNext() == n2
    assert n.getNext().getData() == 10

def test_createList():
    ll = LinkedList()
    assert ll.isEmpty() == True

def test_addNodesToList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)

    assert ll.isEmpty() == False
    assert ll.length() == 3
    assert ll.search(10) == True
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9") == False

def test_removeNodesFromList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    ll.addToFront("CS9")

    assert ll.length() == 4
    assert ll.search("Gaucho") == True
    ll.remove("Gaucho")
    assert ll.search("Gaucho") == False
    assert ll.length() == 3

    assert ll.search(False) == True
    ll.remove(False)
    assert ll.search(False) == False
    assert ll.length() == 2

    assert ll.search(10) == True
    ll.remove(10)
    assert ll.search(10) == False
    assert ll.length() == 1
    assert ll.isEmpty() == False
    ll.remove("CS9")
    assert ll.isEmpty() == True

def test_insertIntoOrderedList():
    ll = LinkedList()
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)

    assert ll.getList() == "10 20 30 35 40 50"

    ll.add(5)
    assert ll.getList() == "5 10 20 30 35 40 50"

    ll.add(60)
    assert ll.getList() == "5 10 20 30 35 40 50 60"