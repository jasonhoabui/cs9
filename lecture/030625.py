'''

BST DELETION

needs a little more attention because we need to preserve the BST property

we can break up deletion in three cases

when the node to be deleted is a leaf node (no children)

when the node to be deleted has one child

when the node to be deleted has two children


case 1:
find the node that needs to be deleted, remove the parent reference (either left child or right child) to the deleted node

case 2: 
connect the deleted node's parent and the deleted node's child together

case 3:
find the successor (node with next greater value) in the right subtree 
this can be done by traversing the left children of the node to be deleted's right subtree 
note that the successor will always only have at most one child 
if the successor had a left child, then it wouldn't be the successor
temporarily store the successor and delete the successor from the tree 
deleting the successor will fall in either case 1 or 1ase 2 
replace the deleted node's value with the successor's value

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

    def delete(self, key):
        if self.size > 1:
            nodetoRemove = self._get(key, self.root)
            if nodetoRemove:
                self.remove(nodetoRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            pass   # NEXT LECTURE
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, \
                    currentNode.leftChild.payload, currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, \
                    currentNode.rightChild.payload, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)
                    
    def inOrder(self, node):
        ret = ""
        if node != None:
            ret += self.inOrder(node.leftChild)
            ret += str(node.key) + " "
            ret += self.inOrder(node.rightChild)
        return ret



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


BST4 = BinarySearchTree()
BST4.put(10, "ten")
assert BST4.inOrder(BST4.root) == "10 "
BST4.delete(10)
assert BST4.size == 0
assert BST4.root == None

BST5 = BinarySearchTree()
BST5.put(10, "ten")
BST5.put(5, "five")
assert BST5.inOrder(BST5.root) == "5 10 "
BST5.delete(10)
assert BST5.inOrder(BST5.root) == "5 "
assert BST5.root.key == 5

BST6 = BinarySearchTree()
BST6.put(10, "ten")
BST6.put(15, "fifteen")
BST6.put(5, "five")
BST6.put(2, "two")
assert BST6.inOrder(BST6.root) == "2 5 10 15 "
BST6.delete(15)
assert BST6.inOrder(BST6.root) == "2 5 10 "

BST7 = BinarySearchTree()
BST7.put(10, "ten")
BST7.put(15, "fifteen")
BST7.put(5, "five")
BST7.put(2, "two")
assert BST7.root.leftChild.key == 5
BST7.delete(5)
assert BST7.inOrder(BST7.root) == "2 10 15 "
assert BST7.root.leftChild.key == 2
assert BST7.root.leftChild.parent.key == 10