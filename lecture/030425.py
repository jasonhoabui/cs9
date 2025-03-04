'''

Binary Search Tree

'''

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key, val):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)


BST1 = BinarySearchTree()
assert BST1.root == None
assert BST1.length() == 0



BST2 = BinarySearchTree()
BST2.put(10, "ten")
assert BST2.root.key == 10
assert BST2.root.payload == "ten"
assert BST2.root.hasLeftChild() == None
assert BST2.root.hasRightChild() == None
assert BST2.root.isLeftChild() == None
assert BST2.root.isRightChild() == None
assert BST2.root.isRoot() == True
assert BST2.root.hasAnyChildren() == None
assert BST2.root.isLeaf() == True
assert BST2.root.hasBothChildren() == None
BST2.root.replaceNodeData(20, "twenty", None, None)
assert BST2.root.key == 20
assert BST2.root.payload == "twenty"



BST3 = BinarySearchTree()
BST3.put(10, "ten")
BST3.put(20, "twenty")
BST3.put(15, "fifteen")
BST3.put(5, "five")
assert BST3.root.key == 10
assert BST3.root.leftChild.key == 5
assert BST3.root.rightChild.key == 20
assert BST3.root.rightChild.leftChild.key == 15