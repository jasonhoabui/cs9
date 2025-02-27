'''
BINARY TREE IMPLEMENTATION


Nodes and References

similar to our Linked List implementation, we can expand upon this concept
using nodes and references to construct our tree
each node can be represented as an object
and each node will have references to other nodes in the tree

'''


class BinaryTreeNode:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else:
            t = BinaryTreeNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else:
            t = BinaryTreeNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key

node = BinaryTreeNode("A")
assert node.getRootValue() == "A"
assert node.getLeftChild() == None
assert node.getRightChild() == None

node = BinaryTreeNode("A")
node.insertLeft("B")
assert node.getRootValue() == "A"
assert node.getLeftChild().getRootValue() == "B"
assert node.getRightChild() == None
assert node.getLeftChild().getLeftChild() == None
assert node.getLeftChild().getRightChild() == None

node = BinaryTreeNode("A")
node.insertLeft("B")
node.insertRight("C")
assert node.getRootValue() == "A"
assert node.getLeftChild().getRootValue() == "B"
assert node.getRightChild().getRootValue() == "C"
assert node.getRightChild().getLeftChild() == None
assert node.getRightChild().getRightChild() == None

node = BinaryTreeNode("A")
node.insertLeft("B")
node.insertLeft("C")
node.insertLeft("D")

temp = node
s = ""
while temp != None:
    s = s + temp.getRootValue()
    temp = temp.getLeftChild()
assert s == "ADCB"



def preorder(tree):
    ret = ""
    if tree != None:
        ret += tree.getRootValue()
        ret += preorder(tree.getLeftChild())
        ret += preorder(tree.getRightChild())
    return ret

def inorder(tree):
    ret = ""
    if tree != None:
        ret += inorder(tree.getLeftChild())
        ret += tree.getRootValue()
        ret += inorder(tree.getRightChild())
    return ret

def postorder(tree):
    ret = ""
    if tree != None:
        ret += postorder(tree.getLeftChild())
        ret += postorder(tree.getRightChild())
        ret += tree.getRootValue()
    return ret

root = BinaryTreeNode("A")
root.insertLeft("D")
root.insertLeft("B")
root.insertRight("C")
root.getRightChild().insertLeft("E")
root.getRightChild().insertRight("F")

assert preorder(root) == "ABDCEF"
assert inorder(root) == "DBAECF"
assert postorder(root) == "DBEFCA"



'''

TREE TRAVERSALS

sometimes we would want to visit all nodes in a tree
we can do this in various ways, and the order of visiting nodes may vary

there are three common recursive ways to traverse nodes in a tree

preorder
visit the node first, the recursively go down left subtree, then recursively go down right subtree

inorder
recursively go down left subtree, visit node, then recursively go down right subtree

postorder
recursively go down left subtree, recursively go down right subtree, then visit node

'''



'''

BINARY SEARCH TREE (BST)

binary trees that have the following properties

values that are less than the parent are in the left subtree
values that are greater than the parent are in the right subtree
this is the "BST property"

BSTs are also one way to implement a "Map" abstract data type

a Map data type maps keys to corresponding values
think of keys defining where in the BST structure a node gets inserte
and each node has a corresponding value field
similar to how Python Dictionaries work at a high level

note: Insertion order affects the structure of the tree
also note: In-order traversal in a BST will visit the nodes in order

'''